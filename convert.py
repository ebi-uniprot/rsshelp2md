#!/usr/bin/env python3
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import base64
import sys
from ftplib import FTP
import pypandoc
import feedparser
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import argparse
import pandas as pd

# Use this to fake a valid user agent for requests
ua = UserAgent()
headers = {'User-Agent': ua.Chrome}

options = Options()
options.headless = True

parser = argparse.ArgumentParser()
parser.add_argument('--input_rss_path', type=str,
                    help='The path to the RSS file to be parsed', required=True)
parser.add_argument('--out_directory', type=str,
                    help='The path to the directory for the resulting converted files to be saved', required=True)
parser.add_argument(
    '--mode', choices=['help', 'news', 'columns', 'context'], help='Determines how the file is processed', required=True)
args = parser.parse_args()

export_path = args.out_directory
images_path = os.path.join(export_path, 'images')
html_path = os.path.join(export_path, 'html')
markdown_path = os.path.join(export_path, 'markdown')
report_path = os.path.join(export_path, 'report')

for p in [images_path, html_path, markdown_path, report_path]:
    Path(p).mkdir(parents=True, exist_ok=True)

uniprot_org_url = 'www.uniprot.org'
uniprot_beta_url = 'beta.uniprot.org'
uniprot_org_kb_path = '/uniprot'
uniprot_beta_kb_path = '/uniprotkb'

re_base64 = re.compile(
    r'data:image\/(?P<image_type>\w+);base64,(?P<image_data>.*)')

table_string = '<table'

image_count = 0

manual_column_mapping = {
    'virus_host': {'uniprotkb': 'virus_hosts'},
    'busco_score': {'proteomes': 'busco'},
    'sequence_status': {'uniprotkb': 'fragment'},

    # 'general_annotation_ALLERGEN': 'cc_allergen'
}


def get_github_image_path(
    image): return f'https://github.com/ebi-uniprot/uniprot-manual/raw/main/images/{image}'


def get_joined_categories(entry):
    if 'tags' in entry:
        return ','.join([tag['term'] for tag in entry['tags']])


def strip_outer_divs(html):
    return html.lstrip('<div>').rstrip('</div>').strip()


def remove_newlines(html):
    return html.replace('\n', ' ')


def replace_see_also_with_ul(parent):
    child = list(parent.children)
    if child[0].text != 'See also:' or not parent.find_all('br'):
        return
    lis = ''.join([f'<li>{el}</li>' for el in child[1:] if el.name != 'br'])
    paragraph = BeautifulSoup(
        f'<p>See also:<ul>{lis}</ul></p>', features='html.parser')
    parent.replace_with(paragraph)


def has_color_style(soup):
    return len(soup.find_all(None, style=lambda value: value and 'color:' in value)) > 0


def convert_html_to_gfm(html, strict=True):
    if strict:
        pandoc_md = pypandoc.convert_text(
            html, 'markdown',
            format='html-native_divs-native_spans', extra_args=['--wrap=none'])
        return pypandoc.convert_text(pandoc_md, 'gfm',
                                     format='markdown', extra_args=['--wrap=none'])
    else:
        return pypandoc.convert_text(html, 'gfm', format='html', extra_args=['--wrap=none'])


def is_image_encoded(src):
    return src.startswith('data:')


def save_image_from_url(src):
    try:
        response = requests.get(src, headers=headers)
        if response.status_code == 200:
            image_file_name = unquote(os.path.basename(src))
            image_file_path = os.path.join(images_path, image_file_name)
            with open(image_file_path, 'wb') as f:
                f.write(response.content)
            return image_file_path
    except requests.Timeout:
        return None


def add_padding_to_encoded_string(image_data):
    return image_data + '=' * (-len(image_data) % 4)


def save_image_from_encoded_string(src, entry_id):
    m = re_base64.match(src)
    assert m
    d = m.groupdict()
    image_type = d['image_type']
    image_data = d['image_data']
    global image_count
    image_count += 1
    image_file_name = f'{entry_id}-{image_count}.{image_type}'
    image_file_path = os.path.join(images_path, image_file_name)
    with open(image_file_path, 'wb') as f:
        f.write(base64.b64decode(add_padding_to_encoded_string(image_data)))
    return image_file_path


def find_and_save_images(soup, entry_id):
    for el in soup.find_all('img'):
        src = el.attrs['src']
        try:
            if is_image_encoded(src):
                image_file_path = save_image_from_encoded_string(src, entry_id)
            else:
                image_file_path = save_image_from_url(src)
        except Exception as e:
            print(el.attrs['src'])
            raise e
        if image_file_path:
            el.attrs['src'] = get_github_image_path(
                os.path.basename(image_file_path))
        else:
            print('Error: No image_file_path', src)


def does_page_exist(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
    except Exception:
        return False
    return response.ok


def is_anchor_in_page(anchor, driver):
    for _ in driver.find_elements_by_id(anchor):
        return True
    return False


def is_ftp_url_ok(parsed):
    try:
        ftp = FTP(parsed.netloc)
        ftp.login()
        path = unquote(parsed.path)
    except:
        return False
    try:
        ftp.cwd(path)
        return True
    except:
        try:
            ftp.size(path)
            return True
        except:
            return False


def is_uniprot_beta_link_ok(parsed):
    url = parsed.geturl()
    assert uniprot_beta_url in url
    driver = webdriver.Chrome(
        options=options, executable_path=os.path.expanduser('~/bin/chromedriver'))
    driver.get(url)
    not_found_class_names = ['message--failure',
                             'error-page-container__art-work']
    for class_name in not_found_class_names:
        if driver.find_elements_by_class_name(class_name):
            return False, None
    if parsed.fragment:
        return True, is_anchor_in_page(parsed.fragment, driver)

    return True, None


def check_and_standardize_link(url, el):
    parsed = urlparse(url)
    # Not checking
    if parsed.scheme == 'ftp':
        return is_ftp_url_ok(parsed), None
    paths = os.path.split(parsed.path)
    # Check if this is uniprot.org
    if parsed.hostname == uniprot_org_url:
        # Check if this uniprot(kb) and if so replace path
        if paths[0] == uniprot_org_kb_path:
            paths = [uniprot_beta_kb_path, *paths[1:]]
            parsed = parsed._replace(path=os.path.join(*paths))
            el.attrs['href'] = parsed.geturl()
        # Check that the corresponding beta page exists
        beta_parsed = parsed._replace(netloc=uniprot_beta_url)
        ok, anchor_found = is_uniprot_beta_link_ok(beta_parsed)
        return ok, anchor_found
    else:
        # Well this isn't ideal but not sure how else to handle this
        # as if the resource is a SPA I won't know what to look for
        # the resource not being able to be accessed
        return does_page_exist(url), None


def check_and_standardize_all_links(soup):
    dead_links = []
    dead_anchors = []
    for el in soup.find_all('a'):
        if 'href' not in el.attrs:
            dead_links.append(f'Anchor tag: {",".join(el.attrs.values())}')
            continue
        url = el.attrs['href']
        ok, anchor_found = check_and_standardize_link(url, el)
        if ok is not None and not ok:
            dead_links.append(url)
        if anchor_found is not None and not anchor_found:
            dead_anchors.append(url)
        print(url, ok, anchor_found)
    return dead_links, dead_anchors


re_sequence_annotation = re.compile(r'sequence_annotation_(.*)')
re_general_annotation = re.compile(r'general_annotation_(.*)')


def get_dict(x): return dict(zip(x.Old, x.New))


df = pd.read_excel('./return-fields-old-to-new.xlsx', sheet_name=None)

for sheet in df.values():
    sheet['Old'] = sheet['Old'].str.lower()

fields_uniprotkb = get_dict(df['uniprotkb'])
fields_uniref = get_dict(df['uniref'])
fields_uniparc = get_dict(df['uniparc'])
fields_proteomes = get_dict(df['proteomes'])

fields = [
    {
        'namespace': 'uniprotkb',
        'fields': fields_uniprotkb
    },
    {
        'namespace': 'uniref',
        'fields': fields_uniref
    },
    {
        'namespace': 'uniparc',
        'fields': fields_uniparc
    },
    {
        'namespace': 'proteomes',
        'fields': fields_proteomes
    },
]


def check_fields(x):
    found = {}
    for d in fields:
        if x in d['fields']:
            found[d['namespace']] = d['fields'][x]
    return found


def convert_return_field(old):
    lower = old.lower()

    found = check_fields(lower)
    if found:
        return found

    lower_spaces = lower.replace('_', ' ')
    found = check_fields(lower_spaces)
    if found:
        return found

    m = re_sequence_annotation.match(lower)
    if m:
        g = m.groups()[0].replace('_', ' ')
        feature = f'feature({g})'
        found = check_fields(feature)
        if found:
            return found

    feature = f'feature({lower_spaces})'
    found = check_fields(feature)
    if found:
        return found

    m = re_general_annotation.match(lower)
    if m:
        g = m.groups()[0].replace('_', ' ')
        comment = f'comment({g})'
        found = check_fields(comment)
        if found:
            return found

    comment = f'comment({lower_spaces})'
    found = check_fields(comment)
    if found:
        return found


def convert(entries, check_links=True, leave_files_with_color_as_html=False):
    for i, entry in enumerate(entries):
        # Use this to resume if something crashes at a particular index
        # if i < 218:
        #     continue
        print(i, entry.id)
        html = entry['content'][0]['value']
        soup = BeautifulSoup(html, features='html.parser')

        with open(os.path.join(html_path, f'{entry.id}.html'), 'w') as f:
            f.write(soup.prettify())

        # If there is a See also: with <br/> separated items replace with <ul>
        for el in soup.find_all(text='See also:'):
            replace_see_also_with_ul(el.parent)

        # Save all images to disk (encoded base64 & urls) with correct img paths
        find_and_save_images(soup, entry.id)

        # Check all links before conversion and if broken, report
        dead_links, dead_anchors = check_and_standardize_all_links(
            soup) if check_links else (None, None)

        html = soup.prettify()

        # Check if page has color style applied and if so don't use strict
        # conversion which removes html tags
        strict = not has_color_style(soup)

        if not strict and leave_files_with_color_as_html:
            left_as_html = True
            md = html
        else:
            left_as_html = False
            md = convert_html_to_gfm(html, strict=strict)

        # Check if there any tables in the markdown
        n_tables_in_html = html.count(table_string)
        n_html_tables_in_md = md.count(table_string)
        n_md_tables_in_md = n_tables_in_html - n_html_tables_in_md
        other_html_tags_left = not strict

        # Save report
        if dead_links or \
           dead_anchors or \
           n_md_tables_in_md or \
           n_html_tables_in_md or \
           other_html_tags_left or \
           left_as_html:
            with open(os.path.join(report_path, f'{entry.id}.txt'), 'w') as f:
                print(entry.id, file=f)
                print('---', file=f)
                if dead_links:
                    print('Dead links',  file=f)
                    print('\n'.join(dead_links),  end='\n\n', file=f)
                if dead_anchors:
                    print('Dead anchor tags',  file=f)
                    print('\n'.join(dead_anchors), end='\n\n', file=f)
                if n_md_tables_in_md:
                    print('Number tables converted to Markdown',  file=f)
                    print(n_md_tables_in_md, end='\n\n', file=f)
                if n_html_tables_in_md:
                    print('Number tables left as HTML',  file=f)
                    print(n_html_tables_in_md, end='\n\n', file=f)
                if other_html_tags_left:
                    print(
                        'All extra HTML tags left (ie <span style="color: grey;">)?', file=f)
                    print(other_html_tags_left, file=f)
                if left_as_html:
                    print('Whole file left as HTML', file=f)
                    print(left_as_html, file=f)

        categories = get_joined_categories(entry)
        # Write Markdown to file
        with open(os.path.join(markdown_path, f'{entry.id}.md'), 'w') as f:
            print('---', file=f)
            print(f'title: {entry["title"]}', file=f)
            if categories:
                print(f'categories: {categories}', file=f)
            print('---', end='\n\n', file=f)
            f.write(md)


def get_help_link(accession):
    return '<Link to={generatePath(LocationToPath[Location.HelpEntry], {accession: "' + accession + '"})}>'


def get_help_accession(url):
    re_help_link = re.compile(r'"https?:\/\/www\.uniprot\.org\/manual\/(.*)"')
    m = re_help_link.match(url)
    return unquote(m.groups()[0])


def replace_anchor_with_link(html):
    re_anchor = re.compile(r'<a href=(.*)>')
    re_open_parenthesis = re.compile(r'\(\n')
    re_close_parenthesis = re.compile(r'\s+\)\n')
    m = re_anchor.search(html)
    if not m:
        return html
    url = m.groups()[0]
    accession = get_help_accession(url)
    link = get_help_link(accession)
    html = re_anchor.sub(link, html)
    html = html.replace('</a>', '</Link>')
    html = re_open_parenthesis.sub('{\' \'}\n', html)
    html = re_close_parenthesis.sub('\n', html)
    return html


def get_feed():
    with open(args.input_rss_path) as f:
        rss = ''.join(f.readlines())
        return feedparser.parse(rss)


def help():
    feed = get_feed()
    convert(feed['entries'])


def news():
    feed = get_feed()
    entries = feed['entries']
    for entry in entries:
        parsed = urlparse(entry['id'])
        entry['id'] = parsed.path[1:].replace('/', '-')
    convert(entries, check_links=False, leave_files_with_color_as_html=True)


def columns():
    feed = get_feed()
    no_column_found = []
    more_than_one_column_found = []
    for entry in feed['entries']:
        parsed = urlparse(entry['id'])
        old = parsed.path[1:]
        converted = convert_return_field(old)
        if not converted:
            if old in manual_column_mapping:
                converted = manual_column_mapping[old]
            else:
                no_column_found.append(old)
                continue
        elif len(converted) > 1:
            more_than_one_column_found.append((old, converted))
            continue
        assert len(converted) == 1, converted
        namespace = list(converted)[0]
        column = converted[namespace]
        html = entry['content'][0]['value']
        soup = BeautifulSoup(html, features='html.parser')
        html = soup.prettify()
        html = replace_anchor_with_link(html)
        html = html.replace('<p>', '<>')
        html = html.replace('</p>', '</>')
        with open(os.path.join(html_path, f'{namespace}.{column}.html'), 'w') as f:
            f.write(html)

    print('No new column found for:')
    for el in no_column_found:
        print(f'{el},')

    print('More than one column found for:')
    for el in more_than_one_column_found:
        print(el)


def get_markdown_for_context_entry(entry):
    parsed = urlparse(entry['id'])
    entry_id = parsed.path[1:] if parsed.path.startswith(
        '/') else parsed.path[1:]
    entry_title = entry['title']
    html = entry['content'][0]['value']
    soup = BeautifulSoup(html, features='html.parser')

    # Check all links before conversion and if broken, report
    dead_links, dead_anchors = check_and_standardize_all_links(
        soup)

    html = soup.prettify()
    md = convert_html_to_gfm(html)
    return f'<h3 id={entry_id}>{entry_title}</h3>\n{md}', dead_links, dead_anchors


def context():
    feed = get_feed()
    dead_anchors = []
    dead_links = []
    with open(os.path.join(markdown_path, 'all.md'), 'w') as f:
        for entry in feed['entries']:
            md, dl, da = get_markdown_for_context_entry(entry)
            if da:
                dead_anchors += da
            if dl:
                dead_links += dl
            print(md, file=f)

    with open(os.path.join(report_path, 'all.txt'), 'w') as f:
        if dead_links:
            print('Dead links:', file=f)
            print('\n'.join(dead_links), file=f)
        if dead_anchors:
            print('Dead anchors:', file=f)
            print('\n'.join(dead_anchors), file=f)

    os.rmdir(images_path)
    os.rmdir(html_path)


def main():
    if args.mode == 'help':
        help()

    if args.mode == 'news':
        news()

    if args.mode == 'columns':
        columns()

    if args.mode == 'context':
        context()


if __name__ == '__main__':
    main()

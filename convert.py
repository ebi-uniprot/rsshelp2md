#!/usr/bin/env python3
import os.path
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import base64
from ftplib import FTP
import pypandoc
import feedparser
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

# Use this to fake a valid user agent for requests
ua = UserAgent()
headers = {'User-Agent': ua.Chrome}

options = Options()
options.headless = True

export_path = './export/pandoc'
images_path = os.path.join(export_path, 'images')
html_path = os.path.join(export_path, 'html')
markdown_path = os.path.join(export_path, 'markdown')
report_path = os.path.join(export_path, 'report')

for p in [images_path, html_path, markdown_path, report_path]:
    Path(p).mkdir(parents=True, exist_ok=True)

uniprotOrgURL = 'www.uniprot.org'
uniprotBetaURL = 'beta.uniprot.org'
uniprotOrgKBPath = '/uniprot'
uniprotBetaKBPath = '/uniprotkb'

table_string = '<table'


def get_joined_categories(entry):
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
            image_file_name = os.path.basename(src)
            image_file_path = os.path.join(images_path, image_file_name)
            with open(image_file_path, 'wb') as f:
                f.write(response.content)
        return image_file_path
    except requests.Timeout:
        return None


def add_padding_to_encoded_string(image_data):
    return image_data + '=' * (-len(image_data) % 4)


def save_image_from_encoded_string(src, image_file_basename):
    re_base64 = re.compile(
        r'data:image\/(?P<image_type>\w+);base64,(?P<image_data>.*)')
    m = re_base64.match(src)
    assert m
    d = m.groupdict()
    image_type = d['image_type']
    image_data = d['image_data']
    image_file_name = f'{image_file_basename}.{image_type}'
    image_file_path = os.path.join(images_path, image_file_name)
    with open(image_file_path, 'wb') as f:
        f.write(base64.b64decode(add_padding_to_encoded_string(image_data)))
    return image_file_path


def find_and_save_images(soup, entry_id):
    encoded_img_counter = 1
    for el in soup.find_all('img'):
        src = el.attrs['src']
        try:
            if is_image_encoded(src):
                image_file_basename = f'{entry_id}-{encoded_img_counter}'
                encoded_img_counter += 1
                image_file_path = save_image_from_encoded_string(
                    src, image_file_basename)
            else:
                image_file_path = save_image_from_url(src)
        except Exception as e:
            print(el.attrs['src'])
            raise e
        el.attrs['src'] = image_file_path


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
    ftp = FTP(parsed.netloc)
    try:
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
    assert uniprotBetaURL in url
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
    if parsed.hostname == uniprotOrgURL:
        # Check if this uniprot(kb) and if so replace path
        if paths[0] == uniprotOrgKBPath:
            paths = [uniprotBetaKBPath, *paths[1:]]
            parsed = parsed._replace(path=os.path.join(*paths))
            el.attrs['href'] = parsed.geturl()
        # Check that the corresponding beta page exists
        beta_parsed = parsed._replace(netloc=uniprotBetaURL)
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
            dead_links.append(','.join(el.attrs.values()))
            continue
        url = el.attrs['href']
        ok, anchor_found = check_and_standardize_link(url, el)
        if ok is not None and not ok:
            dead_links.append(url)
        if anchor_found is not None and not anchor_found:
            dead_anchors.append(url)
        print(url, ok, anchor_found)
    return dead_links, dead_anchors


def main():
    with open('input/help.combined.rss') as f:
        rss = ''.join(f.readlines())
        feed = feedparser.parse(rss)

    for i, entry in enumerate(feed['entries']):
        # if i < 156:
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
        dead_links, dead_anchors = check_and_standardize_all_links(soup)

        html = soup.prettify()

        # Check if page has color style applied and if so don't use strict
        # conversion which removes html tags
        strict = not has_color_style(soup)

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
           other_html_tags_left:
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

        # Write Markdown to file
        with open(os.path.join(markdown_path, f'{entry.id}.md'), 'w') as f:
            print('---', file=f)
            print(f'title: {entry["title"]}', file=f)
            print(f'categories: {get_joined_categories(entry)}', file=f)
            print('---', end='\n\n', file=f)
            f.write(md)


if __name__ == '__main__':
    main()
## To run

Help:

```
./convert.py --input_rss_path=input/help.combined.rss --out_directory=export/help --mode=help
```

Columns:

```
./convert.py --input_rss_path=input/colheaders.rss --out_directory=export/columns --mode=columns
```

## Directory structure

```
./export/{help, columns}/
	html      # The individual HTML files removed from the composite RSS file
	images    # Any images encountered in the HTML
	markdown  # Converted using pandoc
	report    # A report of any issues encountered
```

## Description of `./export/pandoc/report`

### Dead links

These links have been found to not exist in the following way:
If uniprot.org:
If uniprot.org/uniprot:
Swap /uniprot for /uniprotkb
Visit corresponding beta.uniprot.org page and look for 'message--failure' or 'error-page-container\_\_art-work' to determine if the resource exists
Else:
Make request to link with a chrome header and report if it existed. There's an issue here that if the server is just temporarily down at the point of the request it will be deemed so there could be false positive dead links.

### Dead anchor tags (eg #disease-and-drugs)

Only applies to uniprot.org pages. Visits the page and looks in the page to find the anchor tag. If not found it's considered dead.

### Number tables converted to Markdown

The number of tables that were converted by pandoc from HTML into Markdown

### Number tables left as HTML

If a table is too complex pandoc will leave as HTML

### All extra HTML tags left (ie `<span style="color: grey;">`)?

If a color style has been detected then these HTML tags are not stripped

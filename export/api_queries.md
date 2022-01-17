
---
title: Programmatic access - Retrieving entries via queries
categories: UniProtKB,UniRef,UniParc,Programmatic_access,Text_search,Technical,help
---

You can use any query to define the set of entries that you are interested in. Best start with an interactive [text search](http://www.uniprot.org/help/text%2Dsearch) to find the base URL for your set, e.g. all reviewed human entries:

https://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606

or all reviewed entries that were created in the current UniProtKB/Swiss-Prot release:

https://www.uniprot.org/uniprot/?query=reviewed:yes+AND+created:\[current TO \*\]

There are several ways of obtaining the URL corresponding to your query for programmatic use:

*   The URL for the html format with the default column setup can always be found in the browser's location bar.
*   For alternative formats (e.g. fasta, tab-separated), you can click on **Download** to explore the various download formats available for your query. You can request a preview by selecting a format and clicking on **Preview first 10**. In that case, the browser's location bar will contain the URL corresponding to your query and format selections, provided that it is not longer than 1000 characters. All you will have to do before using the URL programmatically is to remove the "&limit=10" part.
*   The **Share** button gives access to the base URL for your query with all the columns in your web view (see also [Customise and share your search results](https://insideuniprot.blogspot.com/2015/03/)). The URL is shown irrespective of its length, even if it may exceed the limitation for the length of GET requests (dependent on client and server software). The default format that this URL generates is the HTML view format. To define a download format, you can append the format of your choice to the URL (i.e. &format=). The table below describes the parameters that you can append to your base URL to retrieve the entries in this format. For example, if you wanted to download the UniProtKB results for 'insulin' with the default columns in tab-separated format:

https://www.uniprot.org/uniprot/?query=insulin&sort=score&columns=id,entry name,reviewed,protein names,genes,organism,length&format=tab  

**Tips**:

*   Get familiar with the [query builder](http://www.uniprot.org/help/advanced%5Fsearch) (advanced search form) by clicking on **Advanced**.
*   Click [**Columns**](http://www.uniprot.org/help/customize) on the search results page to select the columns for retrieving result tables in tab-separated or Excel format.
*   You can also look up your relevant column names in the full list of [UniProtKB column names for programmatic access](http://www.uniprot.org/help/uniprotkb%5Fcolumn%5Fnames).

The URL for a query result consists of a data set name (e.g. `uniprot`, `uniref`, `uniparc`, `taxonomy`, ...) and the actual query. The following query parameters are supported:

Parameter

Values

Description

`query`

_string_

See [query syntax](http://www.uniprot.org/help/text-search)  
  
and [query fields for UniProtKB](http://www.uniprot.org/help/query-fields).  
  
An empty query string will retrieve all entries in a data set. **Tip:** Click **Advanced**  
  
in the search bar.

`format`

`html | tab | xls | fasta | gff | txt | xml | rdf | list | rss`

Format in which to return results:

*   `tab` returns data for the selected `columns` in tab-separated format.
*   `xls` returns data for the selected `columns` for import into Excel.
*   `fasta` returns sequence data only, where applicable.
*   `gff` returns sequence annotation, where applicable.
*   `txt`, `xml` and `rdf` return full entries.
*   `list` returns a list of identifiers.
*   `rss` returns an [OpenSearch](http://opensearch.a9.com/) RSS feed.

**Tip:** Click `Download` above the list of results.

`columns`

comma-separated list of column names

Columns to select for retrieving results in `tab` or `xls` format.  
  
Click **Columns** on the search results page to see the available columns  
  
(for UniProtKB you can also read the [full list of UniProtKB column names](http://www.uniprot.org/help/uniprotkb_column_names)).  
  
**Tip:** Some columns can be parameterized, e.g. `database(PDB)` (see the example at the end of this section).

`include`

`yes | no`

Include isoform sequences when the `format` parameter is set to `fasta`.  
  
Include description of referenced data when the `format` parameter is set to `rdf`.  
  
This parameter is ignored for all other values of the `format` parameter.

`compress`

`yes | no`

Return results gzipped. Note that if the client supports HTTP compression,  
  
results may be compressed transparently even if this parameter is  
  
not set to `yes`.

`limit`

_integer_

Maximum number of results to retrieve.

`offset`

_integer_

Offset of the first result, typically used together with  
  
the `limit` parameter.

The following example retrieves all human entries matching the term '`antigen`' in RDF/XML and tab-separated format, respectively.

https://www.uniprot.org/uniprot/?query=organism:9606+AND+antigen&format=rdf&compress=yes

https://www.uniprot.org/uniprot/?query=organism:9606+AND+antigen&format=tab&compress=yes&columns=id,reviewed,protein names

The next example retrieves all human entries with cross-references to PDB in tab-separated format, showing only the UniProtKB and PDB identifiers.

https://www.uniprot.org/uniprot/?query=organism:9606+AND+database:pdb&format=tab&compress=yes&columns=id,database(PDB)

See also:  
  
[REST API - Access the UniProt website programmatically](http://www.uniprot.org/help/api) - batch retrieval, ID mapping, queries, downloads, etc

Related terms: programmatic access, program, script, wget, curl, web services, API
        

---
title: Is there a download file available where all UniProt IDs from X.laevis are matched to their human equivalents (homologs)? How can I obtain an ortholog mapping of human proteins to S.pombe proteins?
categories: UniProtKB,Text_search,Cross-references,Taxonomy,faq
---

There are no such ready-made files available from UniProt, but a number of phylogenomic databases exist which may be in a better position to answer this question. There is quite a useful [thread on the BioStars website.](http://www.biostars.org/p/7568/)

If you want to use UniProtKB, you should first find out which of the [phylogenomic databases cross-referenced by UniProtKB](http://www.uniprot.org/database/?query=category:%22Phylogenomic+databases%22) provides the best coverage for your organisms.

Once you have selected such a database, e.g. OrthoDB, you can include it in a query that allows you to retrieve all entries from Xenopus laevis and all human Swiss-Prot entries with a cross-reference to the phylogenomic database OrthoDB:

Query: [(organism:"xenopus laevis" or (organism:"homo sapiens" and reviewed:yes)) and database:(type:orthodb)](http://www.uniprot.org/uniprot/?query=%28organism%3a%22xenopus+laevis%22+or+%28organism%3a%22homo+sapiens%22+and+reviewed%3ayes%29+%29+and+database%3a%28type%3aorthodb%29)

Note: To be even more exact, we recommend to use the taxonomy identifiers instead of organism names (e.g. organism:9606).

If you click on the little triangle in the title of the gene name column, you can have these results sorted by gene name, an operation that will group orthologous entries together in many cases:

[https://www.uniprot.org/uniprot/?query=%28organism%3a%22xenopus+laevis%22+or+%28organism%3a9606+and+reviewed%3ayes%29+%29+and+database%3a%28type%3aorthodb%29&sort=genes&desc=no](http://www.uniprot.org/uniprot/?query=%28organism%3a%22xenopus+laevis%22+or+%28organism%3a9606+and+reviewed%3ayes%29+%29+and+database%3a%28type%3aorthodb%29%26sort=genes%26desc=no)

You can customize the table view and add columns for the OrthoDB cross-references. To do this, click on "Columns", go to "Cross-references" and click on "More". Then select the database(s) of interest from the "Phylogenomic databases" section, and click on "Go". You can also remove columns which are not of interest to you in this context.

Once you are happy with the view, click on "Download" and select the tab-separated format.

If you want to sort on the OrthoDB identifiers instead, this cannot be done via the web interface, but once you have downloaded the file, you can open it in Excel and sort there.

See also:  
  
[How is orthology established in UniProtKB/Swiss-Prot?](http://www.uniprot.org/faq/39)  
  
[List of phylogenomic databases cross-referenced in UniProtKB](http://www.uniprot.org/database/?query=category:%22Phylogenomic+databases%22)  
  
[Customize display options](http://www.uniprot.org/help/customize)
        

---
title: UniProtKB filter options
categories: UniProtKB,Text_search,Website,help
---

A search result page is subdivided into a filter panel on the left, and the actual result table on the right, occupying the majority of the screen space.

You can use the filter panel to filter your search results in UniProtKB by **reviewed/unreviewed** status, or by organism, or you can restrict your search terms to certain query fields.

### Organism filters

Under the heading **"Popular organisms"**, your query results are broken down by organism. Filters allow you to see the matches from the 5 best represented organisms among a list of 12 organisms.

These organisms are [Human](http://www.uniprot.org/taxonomy/9606), [Mouse](http://www.uniprot.org/taxonomy/10090), [Rat](http://www.uniprot.org/taxonomy/10116), [Cow](http://www.uniprot.org/taxonomy/9913), [Zebrafish](http://www.uniprot.org/taxonomy/7955), [Drosophila](http://www.uniprot.org/taxonomy/7227), [C.elegans](http://www.uniprot.org/taxonomy/6239), [Slime mold](http://www.uniprot.org/taxonomy/44689), [A.thaliana](http://www.uniprot.org/taxonomy/3702), [Rice](http://www.uniprot.org/taxonomy/39947), [E.coli K12](http://www.uniprot.org/taxonomy/83333), [B.subtilis](http://www.uniprot.org/taxonomy/224308), [S.cerevisiae](http://www.uniprot.org/taxonomy/559292).

If less than 5 of these 12 popular organisms are represented in your result, the organism filters are completed to 5 by iterating over the result set and adding the first encountered organisms as filters. These additional filters are labeled with the 5-letter [UniProtKB organism mnemonic](http://www.uniprot.org/help/taxonomy), while the scientific name appears on mouse-over.

For performance reasons it is currently not possible to provide a **complete** breakdown of query results by organism, since result sets can be huge. A "View by taxonomy" link is available further down the filter panel and provides a similar functionality.

If you are interested in another organism, you can specify its name in the search field under **"Other organisms"**, which supports auto-completion.

### Search term filters

If you have performed a full text search and your search terms can be found in one or more [query fields](http://www.uniprot.org/help/query%2Dfields), you can use the **"Search term"** filters to make your query more specific. This restricts search results to entries which have structured data that exactly matches your term.

#### Notes

*   An active filter is graphically highlighted in the filter panel.

*   All the filters described here can be un-selected by clicking on the cross to their right.

*   Only filters which are valid for your search results will appear. For example, if the search term is not found in the gene name of any of your results, the gene name filter will not appear.

*   Only filters which would further narrow down your search results will appear. For example, in a full text search with [polytrichum commune](http://www.uniprot.org/uniprot/?query=polytrichum%20commune), the result only contains entries from the organism [Polytrichum commune (Haircap moss)](http://www.uniprot.org/taxonomy/3213) and there will not be a filter to restrict the terms to the organism field.

[UniProtKB tutorial/video](https://www.youtube.com/watch?v=ado1r8IDm3U)
        
---
title: Assessing proteome completeness and quality
categories: help
---

In order to assess quality and completeness of [proteomes](http://www.uniprot.org/proteomes) , we provide two values:

-   Statistical evaluation and classification of the proteome by the **Complete Proteome Detector (CPD)** algorithm (developed by UniProt)
-   The [BUSCO score](https://www.sib.swiss/about-sib/news/10131-gauging-the-completeness-of-genomics-data-with-busco) of the proteome, which was developed to quantify genomic data completeness in terms of expected gene content.

### Complete Proteome Detector (CPD)

CPD statistically analyses each proteome against a group of closely related proteomes in order to determine completeness. For each proteome, CPD uses [taxonomic lineage](http://www.uniprot.org/help/taxonomic%5Flineage) information to identify the group of proteomes taxonomically closest to it. A valid group is required to contain a minimum of thirty proteomes and all proteomes in the group must be in the same taxonomic class or more closely related. For the proteome being analyzed, the algorithm considers the quartiles of the protein count of all other proteomes in its group.

This evaluation classifies each proteome into one of six possible categories (in terms of the proteome's protein count vs the protein counts of the other proteomes in its group): **Standard** ; **Close to standard (high value)** ; **Close to standard (low value)** ; **Outlier (high value)** ; **Outlier (low value)** or **Unknown** . The categories are defined by closeness of the protein count to the group median. The closest category to the median is **Standard** , followed by **Close to standard** and then **Outlier** . The subcategories of **high** and **low** reflect whether a proteome has above or below average protein count respectively. Proteomes are marked **unknown** if a score could not be calculated for example if we don't have enough closely related proteomes in the database.

**Score definitions**

Let Q1, Q3 be the first and third quartiles of protein counts of related proteomes and C be the protein count of the proteome being scored.

We define the fences for outliers as:

F <sub>1</sub> = max(0, Q <sub>1</sub> - 1.5 x (Q <sub>3</sub> - Q <sub>1</sub> ))  
F <sub>2</sub> = min(Q <sub>3</sub> + Q <sub>1</sub> , Q <sub>3</sub> + 1.5 x (Q <sub>3</sub> - Q <sub>1</sub> ))

CPD score is defined as:

| status                         | condition                                 |
|:-------------------------------|:------------------------------------------|
| Outlier (low value)            | if C \<= F <sub>1</sub>                   |
| Close to standard (low value)  | if F <sub>1</sub> \< C \< Q <sub>1</sub>  |
| Standard                       | if Q <sub>1</sub> \<= C \< Q <sub>3</sub> |
| Close to standard (high value) | if Q <sub>3</sub> \<= C \< F <sub>2</sub> |
| Outlier (high value)           | if F <sub>2</sub> \<= C                   |

![image](https://github.com/ebi-uniprot/uniprot-manual/raw/main/images/assessing_proteomes-12.png)

Figure 1 caption: *CPD status descriptions are defined by how the protein count of a proteome compares to the distribution of protein counts in a group of at least 30 closely related proteomes. The proteomes chosen for comparison are as closely related as possible in order to find at least 30 proteomes. If not enough proteomes can be found within the same taxonomic class then the proteome is scored "Unknown".*

**Examples**

Example 1 : [Human reference proteome](https://www.uniprot.org/proteomes/UP000005640/) - Score = "Outlier (high)"

The proteome [UP000005640](https://www.uniprot.org/proteomes/UP000005640/) has a protein count of 77027 (as of release 2021_02). When we compare this to the protein counts of closely related proteomes (primates) we can see that this protein count is high. This proteome is scored "Outlier (high)". This is not necessarily a bad sign! The human proteome is very well studied compared to some of the other primate proteomes - so we might expect to see a higher protein count due to all of the identified isoforms due to alternative splicing.

Example 2 : [Human proteome (mitochondrion only)](https://www.uniprot.org/proteomes/UP000307385/) - Score = "Outlier (low)"

This human "proteome" has a very low protein count of 13 (as of release 2021_02). This "proteome" only consists of the proteins encoded in the mitochondrial genome. Therefore a score of "Outlier (low)" makes sense; all other mitochondrial proteins are imported into the organelle but are not reflected in this number.

### Benchmarking Universal Single-Copy Orthologs (BUSCO)

For eukaryotic and bacterial proteomes, we also provide the [BUSCO score](https://www.sib.swiss/about-sib/news/10131-gauging-the-completeness-of-genomics-data-with-busco) , which was developed to quantify genomic data completeness in terms of expected gene content based on single-copy orthologs. We're currently using BUSCO version 4.0.2.

This score includes percentages of complete (C) single-copy (S) genes, complete (C) duplicated (D) genes, fragmented (F) and missing (M) genes, as well as the total number of orthologous clusters (n) used in the BUSCO assessment.

We also report, as is recommended in [BUSCO's user guide](https://busco.ezlab.org/busco%5Fuserguide.html#running-busco-2) , the most specific lineage dataset available to analyse each proteome. For example, to assess fish data we would select the actinopterygii lineage (dataset: actinopterygii_odb10) rather than the metazoa or eukaryota lineage. A full list of available lineage datasets can be found on [BUSCO website](https://busco.ezlab.org/list%5Fof%5Flineages.html) .

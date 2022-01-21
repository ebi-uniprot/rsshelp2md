---
title: UniRef
categories: About_UniProt,UniRef,Similar_proteins,help
---

The UniProt Reference Clusters (UniRef) provide clustered sets of sequences from the [UniProt Knowledgebase](http://www.uniprot.org/help/uniprotkb) (including [isoforms](http://www.uniprot.org/help/canonical%5Fand%5Fisoforms) ) and selected [UniParc](http://www.uniprot.org/help/uniparc) records in order to obtain complete coverage of the sequence space at several resolutions while hiding redundant sequences (but not their descriptions) from view. Unlike in UniParc, sequence fragments are merged in UniRef: The UniRef100 database combines identical sequences and sub-fragments with 11 or more residues from any organism into a single UniRef entry, displaying the sequence of a representative protein, the accession numbers of all the merged entries and links to the corresponding UniProtKB and UniParc records. UniRef90 is built by clustering UniRef100 sequences with 11 or more residues using the **MMseqs2 algorithm** ( [Steinegger M. and Soeding J., Nat. Commun. 9 (2018)](https://www.nature.com/articles/s41467-018-04964-5) ) such that each cluster is composed of sequences that have at least 90% sequence identity to and 80% overlap with the longest sequence (a.k.a. [seed sequence](http://www.uniprot.org/help/uniref%5Fseed) ) of the cluster. Similarly, UniRef50 is built by clustering UniRef90 seed sequences that have at least 50% sequence identity to and 80% overlap with the longest sequence in the cluster. Prior to 2013 there was no overlap threshold, so clusters were more heterogeneous in length. UniRef90 and UniRef50 yield a database size reduction of approximately 58% and 79%, respectively, providing for significantly faster sequence similarity searches. The seed sequence is the longest member of a cluster. However, the longest sequence is not always the most informative. There is often more biologically relevant information (name, function, cross-references) available on other cluster members. All the proteins in a cluster are therefore ranked with the following priority to facilitate the selection of a biologically relevant representative for the cluster:

1.  quality of the entry: [manually reviewed](http://www.uniprot.org/help/manual%5Fcuration) entries (from the UniProtKB/Swiss-Prot section) are preferred
2.  annotation score: entries that have higher UniProtKB [annotation scores](http://www.uniprot.org/help/annotation%5Fscore) are preferred. This also means that UniProtKB entries will always take precedence over entries that are in UniParc but not in UniProtKB (annotation score is undefined in UniParc, which does not contain any annotations).
3.  organism: entries from [reference proteomes](http://www.uniprot.org/help/reference%5Fproteome) and model organisms are preferred
4.  length of the sequence: longest sequence is preferred

### UniRef100

UniRef100 contains all UniProt Knowledgebase records plus selected UniParc records (see below). It is generated by clustering identical sequences and subfragments.

UniRef90 is built based on UniRef100, and UniRef50 is built on UniRef90. However, we leave out sequences shorter than 11 residues from the clustering procedures for UniRef90 and 50, because clusters with these short sequences are very instable in greedy clustering algorithms. The reason we keep these short sequences in UniRef100 is to ensure that UniRef100 completely covers the sequence space, which may be of particular interest to proteomics users.

The UniRef100 identifier is generated by placing a "UniRef100\_" prefix before the UniProtKB accession or UniParc identifier of the representative UniProtKB or UniParc entry, e.g. "UniRef100_P99999" or "UniRef100_UPI0000027233".

In addition to UniProtKB records, UniRef100 also includes the UniParc entries that are not covered by UniProtKB and contains cross-references to the [RefSeq](http://www.ncbi.nlm.nih.gov/refseq/) or [PDB](http://www.wwpdb.org/) databases.

### UniRef90

UniRef90 is generated by clustering UniRef100 seed sequences.

The UniRef100 sequences shorter than 11 residues are excluded in UniRef90 clusters. Each UniRef90 cluster has one representative sequence from the UniRef100 database.

UniRef90 cluster titles and identifiers are derived from the representative UniRef100 entry. The UniRef90 identifier is generated by replacing the "UniRef100\_" prefix of the representative with "UniRef90\_", e.g. "UniRef90_P99999".

### UniRef50

UniRef50 is generated by clustering UniRef90 seed sequences.

UniRef50 cluster titles and identifiers are derived from the representative UniRef90 entry. The UniRef50 identifier is generated by replacing the "UniRef100\_" prefix of the representative with "UniRef50\_", e.g. "UniRef50_P99999".

#### Further information

-   [UniRef FAQ](http://www.uniprot.org/help/?query=category%3AUniRef+AND+section%3Afaq)
-   UniRef Publication [Suzek B.E. et al. (2014)](http://bioinformatics.oxfordjournals.org/content/31/6/926.full)
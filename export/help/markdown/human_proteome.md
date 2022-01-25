---
title: What is UniProt's human proteome?
categories: Proteomes,Download,UniProtKB,Keywords,Sequence,Human,faq
---

In 2008, a draft of the complete human proteome was released from UniProtKB/Swiss-Prot: the approximately 20,000 putative human protein-coding genes were represented by one UniProtKB/Swiss-Prot entry each, tagged with the keyword 'Complete proteome' (now obsolete) and later linked to [proteome identifier](http://www.uniprot.org/manual/proteome%5Fid) [UP000005640](http://www.uniprot.org/proteomes/UP000005640) .

The **UniProtKB/Swiss-Prot *Homo sapiens* proteome** contains one representative ( [canonical](http://www.uniprot.org/help/canonical%5Fand%5Fisoforms) ) protein sequence for each known protein-coding gene. Close to 40% of these 20,000 protein sequence records also contain manually annotated alternative isoforms representing over 22'000 additional sequences (see [What is the canonical sequence? Are all isoforms described in one entry?](http://www.uniprot.org/help/canonical%5Fand%5Fisoforms) ).

-   Query: [proteome:up000005640 AND reviewed:yes](http://www.uniprot.org/uniprotkb/?query=reviewed%3Ayes+AND+proteome%3Aup000005640)

In 2011, a complementary pipeline for import of predicted human protein sequences in UniProtKB/TrEMBL has been developed in collaboration with [Ensembl](http://www.ensembl.org/) to complete the set of human isoform sequences produced by genes present in UniProtKB/Swiss-Prot.

This pipeline works in the following way:

1.  Ensembl sequences are first mapped to their UniProtKB counterparts under stringent conditions, requiring 100% identity over 100% of the length of the two sequences. The thus identified UniProtKB entries are flagged as part of the proteome (via a link to [UP000005640](http://www.uniprot.org/proteomes/up000005640) ) and obtain a cross-reference to the mapped Ensembl record.
2.  Ensembl sequences that are absent from UniProtKB are imported into UniProtKB/TrEMBL. These entries are flagged as part of the proteome and have an Ensembl cross-reference.

This **UniProtKB *H. sapiens* proteome** includes thus both the reviewed sequences from UniProtKB/Swiss-Prot (equivalent to an updated version of the *H. sapiens* proteome completed in 2008), supplemented by unreviewed sequences from UniProtKB/TrEMBL, which may represent additional predicted isoform sequences, but which may potentially also add redundancy.

Query:

-   [proteome:up000005640](http://www.uniprot.org/uniprotkb/?query=proteome%3Aup000005640)

Remark: The number of entries in the human proteome may vary from one release to the other, especially the manually reviewed set. This is due to our continuous manual updates thanks to the availability of new information. On a regular basis, we have to merge entries that were originally thought to be encoded by two separate genes, but later appeared to be actually a single gene. An entry can also be deleted when there is increasing evidence that it is an erroneous translation derived from a pseudogene. We keep dubious sequences in UniProtKB until there is enough evidence to decide whether we should delete them (see [Why do we keep dubious sequences in UniProtKB? How to discard them from a protein set?](http://www.uniprot.org/help/dubious%5Fsequences) ).

**Access to human sequence sets**

Our [FTP server](http://www.uniprot.org/downloads) allows to download expanded FASTA sets, containing both the canonical and manually reviewed isoform sequences, for a selection of the most widely used proteomes, including human.

Below are queries to retrieve different human sequence sets. In order to download the query results, please read [How to retrieve sets of UniProtKB protein sequences?](http://www.uniprot.org/help/retrieve%5Fsets)

You can retrieve:

1\) <u>approximately 20,000 human protein-coding genes represented by the canonical protein sequence</u> in UniProtKB/Swiss-Prot:

-   Query: [proteome:up000005640 AND reviewed:yes](http://www.uniprot.org/uniprotkb/?query=reviewed%3Ayes+AND+proteome%3Aup000005640)

Note: Some of the human entries in UniProtKB/Swiss-Prot are not included in the proteome because their protein sequences do not map to the reference genome:

-   Query: [organism:9606 AND reviewed:yes NOT proteome:up000005640](http://www.uniprot.org/uniprotkb/?query=organism%3A9606+AND+reviewed%3Ayes+NOT+proteome%3Aup000005640)

2\) <u>additional manually reviewed isoform sequences</u> produced by the protein-coding genes described in UniProtKB/Swiss-Prot. There are currently around 22,000 such additional isoform sequences. These are **downloadable in FASTA format** together with the canonical sequences, if you click on "Download" and then select 'FASTA (canonical and isoform)':

-   Query: [proteome:up000005640 AND reviewed:yes](http://www.uniprot.org/uniprotkb/?query=proteome:up000005640+AND+reviewed:yes&format=fasta&include=yes)

3\) <u>additional predicted and unreviewed sequences in UniProtKB/TrEMBL</u> , flagged to be part of the proteome, which may correspond to novel isoform sequences for genes present in UniProtKB/Swiss-Prot (derived from the Ensembl pipeline):

-   Query: [proteome:up000005640 AND reviewed:no](http://www.uniprot.org/uniprotkb/?query=proteome:up000005640+AND+reviewed%3Ano)

Note: Additional human sequences in UniProtKB/TrEMBL are not flagged to be part of the proteome. The vast majority of these additional UniProtKB/TrEMBL entries contain sequences which are not identical to any isoform sequences predicted by Ensembl. They might represent other alternative isoforms. The system is not perfect, but it is the best we can provide for the time being.

-   Query: [organism:9606 AND reviewed:no NOT proteome:up000005640](http://www.uniprot.org/uniprotkb/?query=organism%3A9606+AND+reviewed%3Ano+NOT+proteome:up000005640)

See also:

-   [What are proteomes?](http://www.uniprot.org/help/proteome)
-   [What are reference proteomes?](http://www.uniprot.org/help/reference%5Fproteome)
-   [How to retrieve sets of UniProtKB protein sequences?](http://www.uniprot.org/help/retrieve%5Fsets)
-   [Alternative products](http://www.uniprot.org/manual/alternative%5Fproducts)
-   [Alternative sequence](http://www.uniprot.org/manual/var%5Fseq)

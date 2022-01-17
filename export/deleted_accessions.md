---
title: Why have some UniProtKB accession numbers been deleted? How can I track them?
categories: UniProtKB,Entry_information,UniParc,Release,faq
---

An accession number (AC) is assigned to each protein sequence upon inclusion into UniProtKB. Accession numbers are stable from release to release ( [What is the difference between an accession number (AC) and the entry name?](http://www.uniprot.org/faq/6)). It can however happen that a protein sequence (and its corresponding accession number) is deleted from UniProtKB.

Most **UniProtKB/TrEMBL** deletions are due to the deletion of the corresponding coding sequence (CDS) in the source nucleotide sequence databases EMBL-Bank/DDBJ/GenBank as requested by the original submitters, or due to the deletion of the sequence prediction from Ensembl. It occasionally happens that the same data is resubmitted at a later date, and UniProt works closely with EMBL-Bank/DDBJ/GenBank and Ensembl to ensure appropriate tracking of deletions and updates. However this is not always possible. In addition, some protein sequences are recognized by curators to be Open Reading frames (ORFs) that have been wrongly predicted to code for proteins or to be pseudogenes. When there is enough evidence that these hypothetical proteins are not real, we take the decision to remove them from UniProtKB/TrEMBL.

Another frequent deletion reason in UniProtKB/TrEMBL is [proteome redundancy reduction](http://www.uniprot.org/help/proteome%5Fredundancy).

Deleted entries in **UniProtKB/Swiss-Prot** are mostly Open Reading Frames (ORFs) or pseudogenes that have been wrongly predicted to code for proteins.

Deleted protein sequences can be found in UniParc. Example: [O00597](http://www.uniprot.org/uniprot/O00597) can be found in [UniParc](http://www.uniprot.org/uniparc/UPI000013C29B) (with the tag 'Active=No').

The history of a deleted entry can be tracked (example: [O00597](http://www.uniprot.org/uniprot/O00597?version=)\\* ), and previous entry and sequence versions displayed.

Two documents list the deleted accession numbers:

- [delac\_sp.txt](ftp://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/docs/delac%5Fsp.txt) for deleted ACs in UniProtKB/Swiss-Prot
- [delac\_tr.txt.gz](ftp://ftp.uniprot.org/pub/databases/uniprot/knowledgebase/docs/delac%5Ftr.txt.gz) for deleted ACs in UniProtKB/TrEMBL

See also:

- [What are UniProtKB's criteria for defining a CDS as a protein?](http://www.uniprot.org/faq/25)
- [Does UniProtKB contain all protein sequences?](http://www.uniprot.org/faq/8)
- [Why do we keep dubious sequences in UniProtKB? How to discard them from a protein set?](http://www.uniprot.org/faq/40)
- [How frequently is UniProt released? What is the synchronization delay with other databases?](http://www.uniprot.org/help/synchronization)
- [Accession number](http://www.uniprot.org/manual/accession%5Fnumbers)
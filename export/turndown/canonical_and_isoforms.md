
---
title: What is the canonical sequence? Are all isoforms described in one entry?
categories: UniProtKB,Sequence,Text_search,Download,Technical,faq
---

**What is the canonical sequence?**

To reduce redundancy, the UniProtKB/Swiss-Prot policy is to describe all the protein products encoded by one gene in a given species in a single entry. We choose for each entry a canonical sequence based on at least one of the following criteria:

1.  It is the most prevalent.
2.  It is the most similar to orthologous sequences found in other species.
3.  By virtue of its length or amino acid composition, it allows the clearest description of domains, isoforms, polymorphisms, post-translational modifications, etc.
4.  In the absence of any information, we choose the longest sequence.

Note that for organisms for which the genome sequence is completed, we choose the protein sequence derived from genome translation, unless it is clearly established that a different polymorphism is more frequent for a given position.

Differences to other sequences are documented in the 'Sequence' section (in the flat file FT keys: VAR\_SEQ, CONFLICT, VARIANT, ...). Additional information can be found in the 'Alternative sequence' subsection.

The various UniProtKB distribution formats (Flat Text, XML, RDF/XML) display only the canonical sequence. The website's 'Sequences' section displays the canonical sequence, but for convenience it offers also a view of the isoforms that are described in the 'Alternative sequence' subsection.

**Are all isoforms described in one UniProtKB/Swiss-Prot entry?**

Whenever possible, all the protein products encoded by one gene in a given species are described in a single UniProtKB/Swiss-Prot entry, including isoforms generated by alternative splicing, alternative promoter usage, and alternative translation initiation (\*). However, some alternative splicing isoforms derived from the same gene share only a few exons, if any at all, the same for some 'trans-splicing' events. In these cases, the divergence is obviously too important to merge all protein sequences into a single entry and the isoforms have to be described in separate 'external' entries.

Example: [isoforms derived from the lola gene (Drosophila melanogaster)](http://www.uniprot.org/uniprot/P42284#sequences)

(\*) Important remark: Due to the increase of sequence data coming from large-scale sequencing projects, UniProtKB/TrEMBL may contain additional predicted sequences encoded by genes which are described in a UniProtKB/Swiss-Prot entry.

**How can I retrieve isoform sequences?**

Alternative sequences, described in either single or separate entries, are all available for Blast searches.

Isoform sequences can be downloaded in FASTA format from our [FTP download index page](http://www.uniprot.org/downloads) (choose the file: 'Isoform sequences').

Query-derived sets of canonical sequences alone or canonical and isoform sequences can also be downloaded in FASTA format (see [How to retrieve sets of UniProtKB protein sequences?](http://www.uniprot.org/faq/38)).

See also:

*   [What are UniProtKB's criteria for defining a CDS as a protein?](http://www.uniprot.org/faq/25)
*   [How are protein sequence variety and protein diversity represented in UniProtKB?](http://www.uniprot.org/faq/21)
*   [Sequence length](http://www.uniprot.org/manual/sequence_length)
*   [Alternative products](http://www.uniprot.org/manual/alternative_products)
*   [Alternative sequence](http://www.uniprot.org/manual/var_seq)
*   [Sequence conflict](http://www.uniprot.org/manual/conflict)
        
---
title: Mapping between UniProtKB and NCBI resources (GeneID, RefSeq): how does it work?
categories: UniProtKB,Sequence,Cross-references,faq
---

**How does UniProt do GeneID and RefSeq mappings?**

As per a protocol we have formalized with the NCBI, we create a RefSeq protein-centric mapping. If a UniProtKB protein (canonical or isoform sequence)

-   is 100% identical (over the entire sequence length) to a RefSeq protein and is from the same organism **or**
-   has common EMBL/DDBJ/GenBank **protein** accession numbers (CDS, protein_id)

then that RefSeq accession is mapped to the UniProtKB protein and consequently the entry will also get the corresponding GeneID cross-reference.

**Why are GeneID cross-references absent from some human entries?**

If a UniProtKB protein does not map to a RefSeq Protein, this entry will not have a GeneID cross-reference.

**Why do some GeneID entries link to UniProtKB entries, but those UniProtKB entries do not have the GeneID cross-reference?**

Apart from the UniProtKB-RefSeq mappings that the UniProt Consortium provides to NCBI, and that are reported in 'NCBI Reference Sequences (RefSeq)' section of RefSeq entry reports, NCBI also computes additional 'Related sequences', which can include UniProtKB proteins and are displayed in a separate section.

See also:

-   [Identifier mapping service ('Retrieve/ID mapping')](http://www.uniprot.org/uploadlists)
-   [Cross-references in UniProtKB](http://www.uniprot.org/help/cross-references%5Fin%5Funiprotkb)
-   [Cross-references for isoform sequences](http://www.uniprot.org/help/isoform%5Fcrossreferences)

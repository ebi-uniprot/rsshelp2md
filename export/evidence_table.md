---
title: How can I query UniProtKB annotations by evidence?
categories: UniProtKB,Text_search,faq
---

The table below summarizes the different [evidence types](http://www.uniprot.org/help/evidences) used in UniProtKB annotation, and details how they are labeled in the [Advanced search](http://www.uniprot.org/help/advanced%5Fsearch) menu and in the UniProtKB entry view.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Advanced search** | **ECO\_0000XXX** | **Source** | **Entry view labels** | **Notes** | **Experimental** | **Manual** | **Automatic** |
| **Manual assertions** (in UniProtKB/Swiss-Prot) |  |  |  |  |  |  |  |
| Experimental | ECO\_0000269 | Literature reference | x Publication(s) with "Manual assertion based on experiment in" |  | yes | yes | no |
| Non-traceable author statement | ECO\_0000303 | Literature reference | x Publication(s) with "Manual assertion based on opinion in" |  | yes | yes | no |
| Curator inference | ECO\_0000305 | Literature reference (optional) | Curated, x Publication(s) with "Manual assertion inferred by curator from" |  | no | yes | no |
| Sequence similarity | ECO\_0000250 | Another UniProtKB/Swiss-Prot entry | By similarity |  | no | yes | no |
| Sequence model | ECO\_0000255 | A rule (optional) | Sequence analysis, UniRule annotation, Prosite ProRule annotation, ARBA annotation |  | no | yes | no |
| Combinatorial | ECO\_0000244 | a PDB entry or literature reference (for large-scale proteomics publications) | Combined sources |  | no | yes | no |
| Imported information | ECO\_0000312 | an entry from nucleotide sequence databases, PDB, model organism databases | Imported |  | no | yes | no |
| **Automatic assertions** (in UniProtKB/TrEMBL) |  |  |  |  |  |  |  |
| Sequence model | ECO\_0000256 | a sequence analysis program or an automatic annotation rule | [Sequence analysis](http://www.uniprot.org/help/sam) (SIGNAL, TRANSMEM, COILED or MobiDB-lite), [UniRule annotation](http://www.uniprot.org/help/unirule) (RuleBase, HAMAP or PIRNR/PIRSR), [ARBA annotation](http://www.uniprot.org/help/arba) |  | no | no | yes |
| Combinatorial | ECO\_0000213 | A PDB entry | Combined sources |  | no | no | yes |
| Imported information | ECO\_0000313 | An entry from nucleotide sequence databases (EMBL, Ensembl), PDB, model organism databases | Imported |  | no | no | yes |
| Sequence motif match (InterPro) | ECO\_0000259 | An entry in an InterPro member database | InterPro annotation | used for domain annotation | no | no | yes |
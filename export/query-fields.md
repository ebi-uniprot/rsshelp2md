
---
title: UniProtKB query fields
categories: Text_search,Technical,Website,help
---

Supported query fields for searching specific data in UniProtKB (see also [query syntax](http://www.uniprot.org/help/text-search)).

Field

Example

Description

accession

`[accession:P62988](http://www.uniprot.org/uniprot/?query=accession:P62988)`

Lists all entries with the primary or secondary [accession number](http://www.uniprot.org/manual/accession_numbers) P62988.

active

`[active:no](http://www.uniprot.org/uniprot/?query=active:no)`

Lists all obsolete entries.

annotation

`[annotation:(type:non-positional)](http://www.uniprot.org/uniprot/?query=annotation:(type:non-positional))  
  
[annotation:(type:positional)](http://www.uniprot.org/uniprot/?query=annotation:(type:positional))  
  
[annotation:(type:mod_res "Pyrrolidone carboxylic acid" evidence:experimental)](http://www.uniprot.org/uniprot/?query=annotation%3A%28type%3Amod_res++%22Pyrrolidone+carboxylic+acid%22+evidence%3Aexperimental%29)`

Lists all entries with:

*   any [general annotation (comments \[CC\])](http://www.uniprot.org/help/general_annotation)
*   any [sequence annotation (features \[FT\])](http://www.uniprot.org/help/sequence_annotation)
*   at least one amino acid modified with a Pyrrolidone carboxylic acid group

author

`[author:ashburner](http://www.uniprot.org/uniprot/?query=author:ashburner)`

Lists all entries with at least one reference co-authored by Michael Ashburner.

cdantigen

`[cdantigen:CD233](http://www.uniprot.org/uniprot/?query=cdantigen:CD233)`

Lists all entries whose cluster of differentiation number is CD233 (see [cdlist.txt](http://www.uniprot.org/docs/cdlist)).

chebi

`[chebi:18420](http://www.uniprot.org/uniprot/?query=chebi:18420)`

Lists all entries which are associated with the small molecule corresponding to ChEBI identifier 18420, Mg(2+) (see [How can I search UniProt for chemical or reaction data?](http://www.uniprot.org/help/chemical_data_search)).

citation

`[citation:("intracellular structural proteins")](http://www.uniprot.org/uniprot/?query=citation%3A%28%22intracellular+structural+proteins%22%29)  
  
[citation:(author:ashburner journal:nature)](http://www.uniprot.org/uniprot/?query=citation%3A%28author%3Aashburner+journal%3Anature%29) [citation:9169874](http://www.uniprot.org/uniprot/?query=citation%3A9169874)`

Lists all entries with a [literature citation](http://www.uniprot.org/citations):

*   containing the phrase "intracellular structural proteins" in either title or abstract
*   co-authored by Michael Ashburner and published in Nature
*   with the [PubMed](http://www.ncbi.nlm.nih.gov/pubmed) identifier 9169874

cluster

`[cluster:(uniprot:A5YMT3 identity:0.9)](http://www.uniprot.org/uniprot/?query=cluster%3a(uniprot%3aA5YMT3+AND+identity%3a0.9))`

Lists all entries in the UniRef 90% identity cluster whose representative sequence is UniProtKB entry A5YMT3 ([about UniRef](http://www.uniprot.org/help/uniref)).

count

`[annotation:(type:transmem count:5)](http://www.uniprot.org/uniprot/?query=annotation%3A%28type%3Atransmem+count%3A5%29)  
  
[annotation:(type:transmem count:[5 TO *])](http://www.uniprot.org/uniprot/?query=annotation%3A%28type%3Atransmem+count%3A%5B5+TO+*%5D%29)  
  
[database:(type:pdb count:[20 TO *])](http://www.uniprot.org/uniprot/?query=database%3A%28type%3Apdb+count%3A%5B20+TO+*%5D%29)  
  
`

Lists all entries with:

*   exactly 5 transmembrane regions
*   5 or more transmembrane regions
*   3 or more Cofactor comments
*   20 or more cross-references to PDB

created

`[created:[20121001 TO *]](http://www.uniprot.org/uniprot/?query=created%3A%5B20121001+TO+*%5D)  
  
[reviewed:yes AND created:[current TO *]](http://www.uniprot.org/uniprot/?query=reviewed%3Ayes+AND+created%3A%5Bcurrent+TO+*%5D)`

Lists all entries created since October 1st 2012.  
  
Lists all new UniProtKB/Swiss-Prot entries in the last release.

database

`[database:(type:pfam)](http://www.uniprot.org/uniprot/?query=database:(type:pfam))  
  
[database:(type:pdb 1aut)](http://www.uniprot.org/uniprot/?query=database:(type:pdb%201aut))`

Lists all entries with:

*   a cross-reference to the Pfam database
*   a cross-reference to the PDB database entry 1aut

(see [Databases cross-referenced in UniProtKB](http://www.uniprot.org/docs/dbxref) and [Database mapping](http://www.uniprot.org/help/mapping))

ec

`[ec:3.2.1.23](http://www.uniprot.org/uniprot/?query=ec:3.2.1.23)`

Lists all beta-galactosidases ([Enzyme nomenclature database](http://enzyme.expasy.org/)).

evidence

`[annotation:(type:signal evidence:ECO_0000269)](http://www.uniprot.org/uniprot/?query=annotation%3A%28type%3Asignal+evidence%3AECO_0000269%29)  
  
[(type:mod_res phosphoserine evidence:ECO_0000269)](http://www.uniprot.org/uniprot/?query=annotation%3A(type%3Amod_res+phosphoserine+evidence%3AECO_0000269))  
  
[annotation:(type:function AND evidence:ECO_0000255)](http://www.uniprot.org/uniprot/?query=annotation%3A(type%3Afunction+evidence%3AECO_0000255))`

Lists all entries with:

*   a signal sequence whose positions have been experimentally proven
*   experimentally proven phosphoserine sites
*   a function manually asserted according to rules

(see [Evidence attribution](http://www.uniprot.org/help/evidences))

existence

`[existence:"inferred from homology"](http://www.uniprot.org/uniprot/?query=existence%3A%22inferred+from+homology%22)`

See [Protein existence criteria](http://www.uniprot.org/docs/pe_criteria).

family

`[family:serpin](http://www.uniprot.org/uniprot/?query=family:serpin)`

Lists all entries belonging to the Serpin family of proteins ([Index of protein domains and families](http://www.uniprot.org/docs/similar)).

fragment

`[fragment:yes](http://www.uniprot.org/uniprot/?query=fragment:yes)`

Lists all entries with an incomplete sequence.

gene

`[gene:HPSE](http://www.uniprot.org/uniprot/?query=gene:HPSE)`

Lists all entries for proteins encoded by gene HPSE, but also by HPSE2.

gene\_exact

`[gene_exact:HPSE](http://www.uniprot.org/uniprot/?query=gene_exact:HPSE)`

Lists all entries for proteins encoded by gene HPSE, but excluding variations like HPSE2 or HPSE\_0.

goa

`[goa:(cytoskeleton)](http://www.uniprot.org/uniprot/?query=goa:(cytoskeleton))  
  
[go:0015629](http://www.uniprot.org/uniprot/?query=go:0015629)`

Lists all entries associated with:

*   a GO term containing the word "cytoskeleton"
*   the GO term Actin cytoskeleton and any subclasses

host

`[host:mouse](http://www.uniprot.org/uniprot/?query=host:mouse)  
  
[host:10090](http://www.uniprot.org/uniprot/?query=host:10090)  
  
[host:40674](http://www.uniprot.org/uniprot/?query=host:40674)`

Lists all entries for viruses infecting:

*   organisms with a name containing the word "mouse" (including Arabidopsis thaliana (Mouse-ear cress)!)
*   Mus musculus (Mouse)
*   all mammals (all taxa classified under the taxonomy node for Mammalia)

id

`[id:P00750](http://www.uniprot.org/uniprot/?query=id:P00750)`

Returns the entry with the primary [accession number](http://www.uniprot.org/manual/accession_numbers) P00750.

inchikey

`[inchikey:WQZGKKKJIJFFOK-GASJEMHNSA-N](http://www.uniprot.org/uniprot/?query=inchikey:WQZGKKKJIJFFOK-GASJEMHNSA-N)`

Returns entries associated with the small molecule identified by the [InChIKey](https://en.wikipedia.org/wiki/International_Chemical_Identifier#InChIKey) WQZGKKKJIJFFOK-GASJEMHNSA-N, i.e. D-glucopyranose (see [How can I search UniProt for chemical or reaction data?](http://www.uniprot.org/help/chemical_data_search))

inn

`[inn:Anakinra](http://www.uniprot.org/uniprot/?query=inn:Anakinra)`

Lists all entries whose "International Nonproprietary Name" is Anakinra.

interactor

`[interactor:P00520](http://www.uniprot.org/uniprot/?query=interactor:P00520)`

Lists all entries describing interactions with the protein described by entry P00520.

keyword

`[keyword:toxin](http://www.uniprot.org/uniprot/?query=keyword:toxin)  
  
[keyword:"Toxin [KW-0800]"](http://www.uniprot.org/uniprot/?query=keyword:%22Toxin%20[KW-0800]%22)`

Lists all entries associated with a keyword matching "Toxin" in its name or description ([UniProtKB Keywords](http://www.uniprot.org/keywords)). Lists all entries associated with the UniProtKB keyword [Toxin](http://www.uniprot.org/keywords/KW-0800).

length

`[length:[500 TO 700]](http://www.uniprot.org/uniprot/?query=length%3A%5B500+TO+700%5D)`

Lists all entries describing sequences of length between 500 and 700 residues.

lineage

This field is a synonym for the field `taxonomy`.

mass

`[mass:[500000 TO *]](http://www.uniprot.org/uniprot/?query=mass%3A%5B500000+TO+*%5D)`

Lists all entries describing sequences with a mass of at least 500,000 Da.

method

`[method:maldi](http://www.uniprot.org/uniprot/?query=method:maldi)  
  
[method:xray](http://www.uniprot.org/uniprot/?query=method:maldi)`

Lists all entries for proteins identified by: matrix-assisted laser desorption/ionization (MALDI), crystallography (X-Ray). The `method` field searches names of physico-chemical identification methods in the ['Biophysicochemical properties' subsection](http://www.uniprot.org/help/biophysicochemical_properties) of the ['Function' section](http://www.uniprot.org/help/function_section), the 'Publications' and 'Cross-references' sections.

mnemonic

`[mnemonic:ATP6_HUMAN](http://www.uniprot.org/uniprot/?query=mnemonic:ATP6_HUMAN)`

Lists all entries with entry name (ID) ATP6\_HUMAN. Searches also obsolete entry names ([What is the difference between an accession number (AC) and the entry name?](http://www.uniprot.org/faq/6)).

modified

`[modified:[20120101 TO 20120301]](http://www.uniprot.org/uniprot/?query=modified:[20120101%20TO%2020120301])  
  
[reviewed:yes AND modified:[current TO *]](http://www.uniprot.org/uniprot/?query=reviewed%3Ayes+AND+modified%3A[current+TO+*])`

Lists all entries that were last modified between January and March 2012.  
  
Lists all UniProtKB/Swiss-Prot entries modified in the last release.

name

`[name:"prion protein"](http://www.uniprot.org/uniprot/?query=name%3A%22prion+protein%22)`

Lists all entries for prion proteins.

organelle

`[organelle:Mitochondrion](http://www.uniprot.org/uniprot/?query=organelle:Mitochondrion)`

Lists all entries for proteins encoded by a gene of the mitochondrial chromosome.

organism

`[organism:"Ovis aries"](http://www.uniprot.org/uniprot/?query=organism%3A%22Ovis+aries%22)  
  
[organism:9940](http://www.uniprot.org/uniprot/?query=organism%3A%22Ovis+aries%22)  
  
[organism:sheep](http://www.uniprot.org/uniprot/?query=organism:sheep)  
  
`

Lists all entries for proteins expressed in sheep (first 2 examples) and organisms whose name contains the term "sheep" ([UniProt taxonomy](http://www.uniprot.org/taxonomy)).

plasmid

`[plasmid:ColE1](http://www.uniprot.org/uniprot/?query=plasmid:ColE1)`

Lists all entries for proteins encoded by a gene of plasmid ColE1 ([Controlled vocabulary of plasmids](http://www.uniprot.org/docs/plasmid)).

proteome

`[proteome:UP000005640](http://www.uniprot.org/uniprot/?query=proteome:UP000005640)`

Lists all entries from the human [proteome](http://www.uniprot.org/proteomes).

proteomecomponent

`[proteomecomponent:"chromosome 1" and organism:9606](http://www.uniprot.org/uniprot/?query=proteomecomponent:%22chromosome%201%22+organism%3A%22Homo+sapiens+%28Human%29+[9606]%22)`

Lists all entries from the human chromosome 1.

replaces

`[replaces:P02023](http://www.uniprot.org/uniprot/?query=replaces:P02023)`

Lists all entries that were created from a merge with entry P02023 ([see FAQ](http://www.uniprot.org/faq/6)).

reviewed

`[reviewed:yes](http://www.uniprot.org/uniprot/?query=reviewed:yes)`

Lists all UniProtKB/Swiss-Prot entries ([about UniProtKB](http://www.uniprot.org/help/uniprotkb)).

scope

`[scope:mutagenesis](http://www.uniprot.org/uniprot/?query=scope:mutagenesis)`

Lists all entries containing a reference that was used to gather information about mutagenesis (Entry view: "Cited for", [See 'Publications' section of the user manual](http://www.uniprot.org/manual/references)).

sequence

`[sequence:P05067-9](http://www.uniprot.org/uniprot/?query=sequence:P05067-9)`

Lists all entries containing a link to isoform 9 of the sequence described in entry P05067. Allows searching by specific sequence identifier.

sequence\_modified

`[sequence_modified:[20120101 TO 20120301]](http://www.uniprot.org/uniprot/?query=sequence_modified:[20120101%20TO%2020120301])  
  
[reviewed:yes AND sequence_modified:[current TO *]](http://www.uniprot.org/uniprot/?query=reviewed%3Ayes+AND+sequence_modified%3A[current+TO+*])`

Lists all entries whose sequences were last modified between January and March 2012.  
  
Lists all UniProtKB/Swiss-Prot entries whose sequences were modified in the last release.

strain

`[strain:wistar](http://www.uniprot.org/uniprot/?query=strain:wistar)`

Lists all entries containing a reference relevant to strain wistar ([Lists of strains in reference comments](http://www.uniprot.org/docs/strains) and [Taxonomy help: organism strains](http://www.uniprot.org/help/taxonomy#strain)).

taxonomy

`[taxonomy:40674](http://www.uniprot.org/uniprot/?query=taxonomy:40674)`

Lists all entries for proteins expressed in [Mammals](http://www.uniprot.org/taxonomy/40674). This field is used to retrieve entries for all organisms classified below a given taxonomic node ([taxonomy classification](http://www.uniprot.org/help/taxonomy#lineage)).

tissue

`[tissue:liver](http://www.uniprot.org/uniprot/?query=tissue:liver)`

Lists all entries containing a reference describing the protein sequence obtained from a clone isolated from liver ([Controlled vocabulary of tissues](http://www.uniprot.org/docs/tisslist)).

web

`[web:wikipedia](http://www.uniprot.org/uniprot/?query=web:wikipedia)`

Lists all entries for proteins that are described in [Wikipedia](http://wikipedia.org/).
        
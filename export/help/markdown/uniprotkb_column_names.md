---
title: UniProtKB column names for programmatic access
categories: Technical,Programmatic_access,Text_search,help
---

This documents lists the column names for programmatic (RESTful) access to tab-separated or Excel downloads of UniProtKB search results.

See also:

-   [How can I access resources on this website programmatically?](http://www.uniprot.org/help/api)
-   [Customize display options](http://www.uniprot.org/help/customize)
-   [Customise and share your search results (UniProt blog)](https://insideuniprot.blogspot.com/2015/03/)

### Names & Taxonomy

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Entry                                | id                               |
| Entry name                           | entry name                       |
| Gene names                           | genes                            |
| Gene names (primary)                 | genes(PREFERRED)                 |
| Gene names (synonym)                 | genes(ALTERNATIVE)               |
| Gene names (ordered locus)           | genes(OLN)                       |
| Gene names (ORF)                     | genes(ORF)                       |
| Organism                             | organism                         |
| Organism ID                          | organism-id                      |
| Protein names                        | protein names                    |
| Proteomes                            | proteome                         |
| Taxonomic lineage                    | lineage(ALL)                     |
| Virus hosts                          | virus hosts                      |

### Sequences

| Column names as displayed on website | Column names as displayed in URL         |
|:-------------------------------------|:-----------------------------------------|
| Fragment                             | fragment                                 |
| Gene encoded by                      | encodedon                                |
| Alternative products                 | comment(ALTERNATIVE PRODUCTS)            |
| Erroneous gene model prediction      | comment(ERRONEOUS GENE MODEL PREDICTION) |
| Erroneous initiation                 | comment(ERRONEOUS INITIATION)            |
| Erroneous termination                | comment(ERRONEOUS TERMINATION)           |
| Erroneous translation                | comment(ERRONEOUS TRANSLATION)           |
| Frameshift                           | comment(FRAMESHIFT)                      |
| Mass spectrometry                    | comment(MASS SPECTROMETRY)               |
| Polymorphism                         | comment(POLYMORPHISM)                    |
| RNA editing                          | comment(RNA EDITING)                     |
| Sequence caution                     | comment(SEQUENCE CAUTION)                |
| Length                               | length                                   |
| Mass                                 | mass                                     |
| Sequence                             | sequence                                 |
| Alternative sequence                 | feature(ALTERNATIVE SEQUENCE)            |
| Natural variant                      | feature(NATURAL VARIANT)                 |
| Non-adjacent residues                | feature(NON ADJACENT RESIDUES)           |
| Non-standard residue                 | feature(NON STANDARD RESIDUE)            |
| Non-terminal residue                 | feature(NON TERMINAL RESIDUE)            |
| Sequence conflict                    | feature(SEQUENCE CONFLICT)               |
| Sequence uncertainty                 | feature(SEQUENCE UNCERTAINTY)            |
| Sequence version                     | version(sequence)                        |

### Function

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Absorption                           | comment(ABSORPTION)              |
| Active site                          | feature(ACTIVE SITE)             |
| Binding site                         | feature(BINDING SITE)            |
| Catalytic activity                   | comment(CATALYTIC ACTIVITY)      |
| ChEBI                                | chebi                            |
| ChEBI (Catalytic activity)           | chebi(Catalytic activity)        |
| ChEBI (Cofactor)                     | chebi(Cofactor)                  |
| ChEBI IDs                            | chebi-id                         |
| Cofactor                             | comment(COFACTOR)                |
| DNA binding                          | feature(DNA BINDING)             |
| EC number                            | ec                               |
| Enzyme regulation                    | comment(ENZYME REGULATION)       |
| Function \[CC\]                      | comment(FUNCTION)                |
| Kinetics                             | comment(KINETICS)                |
| Metal binding                        | feature(METAL BINDING)           |
| Nucleotide binding                   | feature(NP BIND)                 |
| Pathway                              | comment(PATHWAY)                 |
| pH dependence                        | comment(PH DEPENDENCE)           |
| Redox potential                      | comment(REDOX POTENTIAL)         |
| Rhea ids                             | rhea-id                          |
| Site                                 | feature(SITE)                    |
| Temperature dependence               | comment(TEMPERATURE DEPENDENCE)  |

### Miscellaneous

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Annotation score                     | annotation score                 |
| Features                             | features                         |
| Caution                              | comment(CAUTION)                 |
| Miscellaneous \[CC\]                 | comment(MISCELLANEOUS)           |
| Keywords                             | keywords                         |
| Matched text                         | context                          |
| Protein existence                    | existence                        |
| Tools                                | tools                            |
| Reviewed                             | reviewed                         |

### Interaction

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Subunit structure \[CC\]             | comment(SUBUNIT)                 |
| Interacts with                       | interactor                       |

### Expression

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Developmental stage                  | comment(DEVELOPMENTAL STAGE)     |
| Induction                            | comment(INDUCTION)               |
| Tissue specificity                   | comment(TISSUE SPECIFICITY)      |

### Gene Ontology (GO)

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Gene ontology (GO)                   | go                               |
| Gene ontology (biological process)   | go(biological process)           |
| Gene ontology (molecular function)   | go(molecular function)           |
| Gene ontology (cellular component)   | go(cellular component)           |
| Gene ontology IDs                    | go-id                            |

### Pathology & Biotech

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Allergenic properties                | comment(ALLERGEN)                |
| Biotechnological use                 | comment(BIOTECHNOLOGY)           |
| Disruption phenotype                 | comment(DISRUPTION PHENOTYPE)    |
| Involvement in disease               | comment(DISEASE)                 |
| Pharmaceutical use                   | comment(PHARMACEUTICAL)          |
| Toxic dose                           | comment(TOXIC DOSE)              |

### Subcellular location

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Subcellular location \[CC\]          | comment(SUBCELLULAR LOCATION)    |
| Intramembrane                        | feature(INTRAMEMBRANE)           |
| Topological domain                   | feature(TOPOLOGICAL DOMAIN)      |
| Transmembrane                        | feature(TRANSMEMBRANE)           |

### PTM / Processsing

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Post-translational modification      | comment(PTM)                     |
| Chain                                | feature(CHAIN)                   |
| Cross-link                           | feature(CROSS LINK)              |
| Disulfide bond                       | feature(DISULFIDE BOND)          |
| Glycosylation                        | feature(GLYCOSYLATION)           |
| Initiator methionine                 | feature(INITIATOR METHIONINE)    |
| Lipidation                           | feature(LIPIDATION)              |
| Modified residue                     | feature(MODIFIED RESIDUE)        |
| Peptide                              | feature(PEPTIDE)                 |
| Propeptide                           | feature(PROPEPTIDE)              |
| Signal peptide                       | feature(SIGNAL)                  |
| Transit peptide                      | feature(TRANSIT)                 |

### Structure

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| 3D                                   | 3d                               |
| Beta strand                          | feature(BETA STRAND)             |
| Helix                                | feature(HELIX)                   |
| Turn                                 | feature(TURN)                    |

### Publications

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Mapped PubMed ID                     | citationmapping                  |
| PubMed ID                            | citation                         |

### Date of

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Date of creation                     | created                          |
| Date of last modification            | last-modified                    |
| Date of last sequence modification   | sequence-modified                |
| Entry version                        | version(entry)                   |

### Family & Domains

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Domain \[CC\]                        | comment(DOMAIN)                  |
| Sequence similarities                | comment(SIMILARITY)              |
| Protein families                     | families                         |
| Coiled coil                          | feature(COILED COIL)             |
| Compositional bias                   | feature(COMPOSITIONAL BIAS)      |
| Domain \[FT\]                        | feature(DOMAIN EXTENT)           |
| Motif                                | feature(MOTIF)                   |
| Region                               | feature(REGION)                  |
| Repeat                               | feature(REPEAT)                  |
| Zinc finger                          | feature(ZINC FINGER)             |

### Taxonomic lineage

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| Taxonomic lineage (all)              | lineage(all)                     |
| Taxonomic lineage (SUPERKINGDOM)     | lineage(SUPERKINGDOM)            |
| Taxonomic lineage (KINGDOM)          | lineage(KINGDOM)                 |
| Taxonomic lineage (SUBKINGDOM)       | lineage(SUBKINGDOM)              |
| Taxonomic lineage (SUPERPHYLUM)      | lineage(SUPERPHYLUM)             |
| Taxonomic lineage (PHYLUM)           | lineage(PHYLUM)                  |
| Taxonomic lineage (SUBPHYLUM)        | lineage(SUBPHYLUM)               |
| Taxonomic lineage (SUPERCLASS)       | lineage(SUPERCLASS)              |
| Taxonomic lineage (CLASS)            | lineage(CLASS)                   |
| Taxonomic lineage (SUBCLASS)         | lineage(SUBCLASS)                |
| Taxonomic lineage (INFRACLASS)       | lineage(INFRACLASS)              |
| Taxonomic lineage (SUPERORDER)       | lineage(SUPERORDER)              |
| Taxonomic lineage (ORDER)            | lineage(ORDER)                   |
| Taxonomic lineage (SUBORDER)         | lineage(SUBORDER)                |
| Taxonomic lineage (INFRAORDER)       | lineage(INFRAORDER)              |
| Taxonomic lineage (PARVORDER)        | lineage(PARVORDER)               |
| Taxonomic lineage (SUPERFAMILY)      | lineage(SUPERFAMILY)             |
| Taxonomic lineage (FAMILY)           | lineage(FAMILY)                  |
| Taxonomic lineage (SUBFAMILY)        | lineage(SUBFAMILY)               |
| Taxonomic lineage (TRIBE)            | lineage(TRIBE)                   |
| Taxonomic lineage (SUBTRIBE)         | lineage(SUBTRIBE)                |
| Taxonomic lineage (GENUS)            | lineage(GENUS)                   |
| Taxonomic lineage (SUBGENUS)         | lineage(SUBGENUS)                |
| Taxonomic lineage (SPECIES GROUP)    | lineage(SPECIES GROUP)           |
| Taxonomic lineage (SPECIES SUBGROUP) | lineage(SPECIES SUBGROUP)        |
| Taxonomic lineage (SPECIES)          | lineage(SPECIES)                 |
| Taxonomic lineage (SUBSPECIES)       | lineage(SUBSPECIES)              |
| Taxonomic lineage (VARIETAS)         | lineage(VARIETAS)                |
| Taxonomic lineage (FORMA)            | lineage(FORMA)                   |

### Taxonomic identifier

| Column names as displayed on website    | Column names as displayed in URL |
|:----------------------------------------|:---------------------------------|
| Taxonomic identifier (all)              | lineage-id(all)                  |
| Taxonomic identifier (SUPERKINGDOM)     | lineage-id(SUPERKINGDOM)         |
| Taxonomic identifier (KINGDOM)          | lineage-id(KINGDOM)              |
| Taxonomic identifier (SUBKINGDOM)       | lineage-id(SUBKINGDOM)           |
| Taxonomic identifier (SUPERPHYLUM)      | lineage-id(SUPERPHYLUM)          |
| Taxonomic identifier (PHYLUM)           | lineage-id(PHYLUM)               |
| Taxonomic identifier (SUBPHYLUM)        | lineage-id(SUBPHYLUM)            |
| Taxonomic identifier (SUPERCLASS)       | lineage-id(SUPERCLASS)           |
| Taxonomic identifier (CLASS)            | lineage-id(CLASS)                |
| Taxonomic identifier (SUBCLASS)         | lineage-id(SUBCLASS)             |
| Taxonomic identifier (INFRACLASS)       | lineage-id(INFRACLASS)           |
| Taxonomic identifier (SUPERORDER)       | lineage-id(SUPERORDER)           |
| Taxonomic identifier (ORDER)            | lineage-id(ORDER)                |
| Taxonomic identifier (SUBORDER)         | lineage-id(SUBORDER)             |
| Taxonomic identifier (INFRAORDER)       | lineage-id(INFRAORDER)           |
| Taxonomic identifier (PARVORDER)        | lineage-id(PARVORDER)            |
| Taxonomic identifier (SUPERFAMILY)      | lineage-id(SUPERFAMILY)          |
| Taxonomic identifier (FAMILY)           | lineage-id(FAMILY)               |
| Taxonomic identifier (SUBFAMILY)        | lineage-id(SUBFAMILY)            |
| Taxonomic identifier (TRIBE)            | lineage-id(TRIBE)                |
| Taxonomic identifier (SUBTRIBE)         | lineage-id(SUBTRIBE)             |
| Taxonomic identifier (GENUS)            | lineage-id(GENUS)                |
| Taxonomic identifier (SUBGENUS)         | lineage-id(SUBGENUS)             |
| Taxonomic identifier (SPECIES GROUP)    | lineage-id(SPECIES GROUP)        |
| Taxonomic identifier (SPECIES SUBGROUP) | lineage-id(SPECIES SUBGROUP)     |
| Taxonomic identifier (SPECIES)          | lineage-id(SPECIES)              |
| Taxonomic identifier (SUBSPECIES)       | lineage-id(SUBSPECIES)           |
| Taxonomic identifier (VARIETAS)         | lineage-id(VARIETAS)             |
| Taxonomic identifier (FORMA)            | lineage-id(FORMA)                |

### Cross-references

| Column names as displayed on website | Column names as displayed in URL |
|:-------------------------------------|:---------------------------------|
| db\_abbrev                           | database(db\_abbrev)             |
| e.g.??EMBL                            | database(EMBL)                   |

where `db_abbrev` can be found in the "Abbrev:" field of the document [Databases cross-referenced in UniProtKB](http://www.uniprot.org/docs/dbxref) .

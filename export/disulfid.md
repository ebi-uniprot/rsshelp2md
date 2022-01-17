---
title: Disulfide bond
categories: PTM_processing,manual
---

This subsection of the PTM / Processing":/help/ptm\_processing\_section section describes the positions of cysteine residues participating in disulfide bonds.

Disulfide bond formation generally occurs in the endoplasmic reticulum by oxidation. Therefore disulfide bonds are mostly found in extracellular, secreted and periplasmic proteins, although they can also be formed in cytoplasmic proteins under conditions of oxidative stress.

In UniProtKB, we annotate intrachain and interchain disulfide bonds and redox-active centres. We annotate both experimentally determined disulfide bonds and predicted disulfide bonds which occur in specific protein families.

If the position of one amino acid involved in the bond is not known, a question mark may be written in the position field instead. It is frequently the case for fragments, when one of the Cys residues is missing.

Example: [P10846](http://www.uniprot.org/uniprot/P10846#ptm%5Fprocessing)

### 1\. Intrachain disulfide bonds

Intrachain disulfide bonds are formed between two cysteines within the same protein chain.

Example: [Q43495](http://www.uniprot.org/uniprot/Q43495#ptm_processing)

Intrachain disulfide bonds are usually conserved and can be propagated 'By similarity' to homologous proteins.

Example: [P18844](http://www.uniprot.org/uniprot/P18844#ptm%5Fprocessing)

In some cases, it is unclear which cysteines participate in disulfide bond formation. In these cases, we indicate the possible alternate bonds which form using the syntax 'or C-X with C-Y'.

Example: [Q9U8R2](http://www.uniprot.org/uniprot/Q9U8R2#ptm%5Fprocessing)

When available, specific information regarding the properties or the function of a specific disulfide bond is indicated.

Examples: [P19880](http://www.uniprot.org/uniprot/P19880#ptm_processing), [P09478](http://www.uniprot.org/uniprot/P09478#ptm_processing)

### 2\. Interchain disulfide bonds (between homo- and heterodimers)

Interchain disulfide bonds are formed between two cysteines of individual chains of the same protein or between two cysteines of distinct proteins. We explicitly describe interchain disulfide bonds giving the name of the second protein or chain (if it is different), and specifying the position of the second cysteine within that protein or chain.

#### a. Disulfide bonds between homodimers

Interchain disulfide bonds within a homodimer are annotated as 'Interchain' in the 'Description' field, not specifying the name of the partner protein. The disulfide linkage is also described in the ' [Subunit](http://www.uniprot.org/manual/subunit)' subsection of the 'Interaction' section.

Examples: [P25703](http://www.uniprot.org/uniprot/P25703#ptm_processing) (Parallel homodimer), [P83658](http://www.uniprot.org/uniprot/P83658#ptm_processing) (Antiparallel homodimer)

#### b. Disulfide bonds between 2 chains or peptides from the same protein precursor

Disulfide bonds formed between 2 proteolytically generated parts of the same protein are considered as interchain. The 2 chains are named in the 'Description' field using the syntax 'between X and Y'. Note that the names of all cleavage products are given in the ' [Protein names](http://www.uniprot.org/manual/protein_names)' subsection of the [Names and taxonomy](http://www.uniprot.org/help/names%5Fand%5Ftaxonomy%5Fsection) section.

Example: [P11140](http://www.uniprot.org/uniprot/P11140#ptm_processing)

A few proteins form an intrachain disulfide bond when monomeric, and an interchain disulfide bond when dimeric.

Example: [P68432](http://www.uniprot.org/uniprot/P68432#ptm_processing)

#### c. Disulfide bonds between heterodimers

Disulfide bonds between cysteines of distinct proteins are described in a complementary way in both entries involved.

For example, botrocetin alpha and beta chains form a heterodimer linked by a disulfide bond, this bond is described in the entry of botrocetin alpha chain and in that of the beta chain.

Example: [P22030](http://www.uniprot.org/uniprot/P22030#ptm_processing) (alpha chain), [P22029](http://www.uniprot.org/uniprot/P22029#ptm_processing) (beta chain).

If the position of the cysteine on the partner chain is unknown, we only indicate the name of the partner protein.

Example: [O35348](http://www.uniprot.org/uniprot/O35348#ptm_processing)

In some cases, it is unclear which cysteines of the partner protein participate in disulfide bond formation; in these cases, we indicate the possible cysteines involved in the bond using the syntax 'or C-X with C-Y'.

Example: [P09930](http://www.uniprot.org/uniprot/P09930#ptm_processing)

### 3\. Redox-active centers

Some disulfide bonds constitute a redox-active center and participate directly in redox reactions, usually via reversible oxidation of a

cysteine residue leading to a cysteine-sulfenic acid.

Examples: [Q96HE7](http://www.uniprot.org/uniprot/Q96HE7#ptm_processing), [Q06530](http://www.uniprot.org/uniprot/Q06530#ptm_processing)

Related keyword: [Redox-active center](http://www.uniprot.org/keywords/676)

### 4\. Annotation of predicted disulfide bonds

Some domains, such as Ig-like and C-lectin domains, are known to contain intrachain disulfide bonds formed between conserved cysteines. The positions of the potential disulfide bonds can therefore be predicted based on the alignment of individual sequences with the profiles describing such domains. These predicted disulfide bonds are tagged with the qualifier 'By similarity'.

Example: [Q865R3](http://www.uniprot.org/uniprot/Q865R3#ptm_processing)
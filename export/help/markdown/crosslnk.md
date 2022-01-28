---
title: Cross-link
categories: PTM_processing,manual
---

This subsection of the [PTM / Processing](http://www.uniprot.org/help/ptm%5Fprocessing%5Fsection) section describes **covalent linkages** of various types formed **between two proteins (interchain cross-links)** or **between two parts of the same protein (intrachain cross-links)** , except the disulfide bonds that are annotated in the ['Disulfide bond'](https://www.uniprot.org/help/disulfid) subsection.

Interchain cross-links are involved in the formation of covalently linked protein complexes. Common cross-links include ubiquitin (and ubiquitin-like)(Ubl) conjugation, SUMOylation, transglutamination, thioether bonds and thioester bonds.

For each cross-link, we specify the name of the conjugate and the identity of the two amino acids involved in the 'Description' field. There is a strict controlled vocabulary for the description of cross-link types.

### 1. Intrachain cross-links {\#1\_\_Intrachain\_cross\_links}

For intrachain cross-links, we cite the amino acids involved in their order of appearance in the sequence.  
Examples: [P36503](https://www.uniprot.org/uniprotkb/p36503#ptm_processing) , [P36499](https://www.uniprot.org/uniprotkb/p36499#ptm_processing)

Note that the intrachain cross-link of the C-terminus with the N-terminus results in the formation of a cyclopeptide:  
Example: [O07623](https://www.uniprot.org/uniprotkb/o07623#ptm_processing)

### 2. Interchain cross-links {\#2\_\_Interchain\_cross\_links}

For interchain cross-links we give the identity of the two amino acids involved, the amino acid in the partner protein cited in second position. We also indicate that the linkage is interchain and provide the name of the partner protein.  
Examples: [P16893](https://www.uniprot.org/uniprotkb/p16893#ptm_processing) , [P08697](https://www.uniprot.org/uniprotkb/p08697#ptm_processing) , [P02671](https://www.uniprot.org/uniprotkb/p02671#ptm_processing)

#### a. Cross-link between homodimers

Cross-links between individual subunits of a homodimer are annotated as interchain cross-links and use the same syntax as above, except that the name of the protein is not indicated.  
Example: [P02679](https://www.uniprot.org/uniprotkb/p02679#ptm_processing)

#### b. Cross-links between two chains or peptides from the same protein precursor

Cross-links formed between two proteolytically generated parts of the same protein are annotated as interchain. The identities of the two chains are indicated in the 'Description' field using the syntax 'between chain A and chain B'.

### 3. Other common cross-links {\#3\_\_Other\_common\_cross\_links}

-   Ubiquitin-like (Ubl) conjugation
-   Transglutamination
-   Thioether bond
-   Thioester bond
-   Special cases

#### a. Ubiquitin and Ubiquitin-like conjugation

Ubiquitin (Ubl) conjugation includes conjugation of ubiquitin and of related proteins, which are collectively referred to as modifiers. Ubl conjugation requires the concerted action of several enzymes which act in a stepwise process. Ubl is activated by an E1 ubiquitin-activating enzyme and then transferred from E1 to the active site cysteine of a Ubl-conjugating enzyme E2. The final step of the ubiquitylation process generally requires the activity of a specific E3 ubiquitin-protein ligase, which functions as a specific substrate recognition module of the system. Ubl conjugation is reversible.

Related keyword: [Ubl conjugation](http://www.uniprot.org/keywords/832)  
Note that the keyword ['Ubl conjugation pathway'](http://www.uniprot.org/keywords/833) is applied to proteins involved in conjugating/deconjugating the Ubl, and not to the ubl conjugation target proteins.

**Ubiquitination**  
Ubiquitination often leads to the degradation of the modified protein by the proteasome.

Example of target: [Q04119](https://www.uniprot.org/uniprotkb/q04119#ptm%5Fprocessing)

Example of modifier: [P62990](https://www.uniprot.org/uniprotkb/p62990#ptm%5Fprocessing)

**Sumoylation**  
Sumoylation is involved in the nuclear retention of proteins that normally shuttle between the nucleus and cytoplasm and in the targeting of proteins to specific subnuclear structures.

Example of target: [Q9H2X6](https://www.uniprot.org/uniprotkb/q9h2x6#ptm_processing)

Example of modifier: [P63165](https://www.uniprot.org/uniprotkb/p63165#ptm_processing)

**Atg12 conjugation**  
This conjugation is essential for autophagy. Atg5 is the unique substrate.

Example of target: [Q9H1Y0](https://www.uniprot.org/uniprotkb/q9h1y0#ptm_processing)

Example of modifier: [O94817](https://www.uniprot.org/uniprotkb/o94817#ptm_processing)

**Neddylation**  
Neddylation is the conjugation of NEDD8 (known as 'Rub' in plants). The substrates are proteins of the cullin family, that are themselves E3 enzymes involved in ubiquitination. Neddylation of cullins may control ubiquitination level.

Example of target: [Q94AH6](https://www.uniprot.org/uniprotkb/q94ah6#ptm_processing)

Example of modifier: [Q9SHE7](https://www.uniprot.org/uniprotkb/q9she7#ptm_processing)

#### b. Transglutamination

Transglutamination is catalyzed by transglutaminases that cross-link glutamine with lysine. Under physiological conditions, tranglutamination of intermediate filaments and their associated proteins is essential for the formation of the protective cornified cell envelope that contributes to the structure of the skin barrier. Aberrant non-reversible transglutamination is implicated in various diseases of the skin and in Alzheimer disease.

Protein 1: [P02671](https://www.uniprot.org/uniprotkb/p02671#ptm_processing)

Protein 2: [P08697](https://www.uniprot.org/uniprotkb/p08697#ptm_processing)

#### c. Thioether bond

Thioether bond type cross-links are mainly found in antimicrobial peptides, or lantibiotics. Lantibiotic thioether bonds are formed between a cysteine and a threonine or a serine.  
Example: [P36503](https://www.uniprot.org/uniprotkb/p36503#ptm_processing)

Related keyword: [Thioether bond](http://www.uniprot.org/keywords/883)

#### d. Thioester bond

Thioester bonds are formed between a cysteine and a glutamine; they are mainly found in eukaryotic proteins.  
Example: [P14046](https://www.uniprot.org/uniprotkb/p14046#ptm_processing)

Related keyword: [Thioester bond](http://www.uniprot.org/keywords/882)

#### e. Special cases

Some cross-links may involve the rare [non-standard amino acid](http://www.uniprot.org/help/non%5Fstd) **selenocysteine** . Others may form between amino acids that undergo preliminary modification(s) prior to cross-link formation.  
Example: [Q9MYY8](https://www.uniprot.org/uniprotkb/q9myy8#ptm_processing) (Selenocysteine)

**Tryptophan tryptophylquinone (TTQ)** is formed by oxidation of the indole ring of a tryptophan to form tryptophylquinone followed by covalent cross-linking with another tryptophan residue.  
Example: [P00372](https://www.uniprot.org/uniprotkb/p00372#ptm_processing)  
Related keyword: [TTQ](http://www.uniprot.org/keywords/824)

Analagous cross-links have been observed between tryptophylquinone and cysteine (related keyword: [CTQ](http://www.uniprot.org/keywords/885) ) and between tyrosylquinone and lysine (related keyword: [LTQ](http://www.uniprot.org/keywords/886) ).

See also the subsection [Post-translational modifications](http://www.uniprot.org/help/post-translational%5Fmodification) for additional information on modifications for which **position-specific data is not yet available** .

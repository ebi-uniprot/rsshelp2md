---
title: Sequence annotation (Features)
categories: manual
---

Sequence annotations describe regions or sites of interest in the protein sequence, such as post-translational modifications, binding sites, enzyme active sites, local secondary structure or other characteristics reported in the cited references. Sequence conflicts between references are also described in this manner.

Sequence annotations (position-specific annotations) used to be found in the 'Sequence annotation (Features)' section in the previous version of the UniProtKB entry view. The flat file and XML formats still group all position-specific annotation together in a "feature table" (FT, ). Each sequence annotation consists of a "feature key", "from" and "to" positions as well as a short description.

The current entry view displays annotation by subject (Function, PTM & processing, etc), and the various position-specific annotations are now distributed to the relevant new sections.

|     |     |
| --- | --- |
| **Subsection** | **Content** |
| **Molecule processing** |
| [Initiator methionine](http://www.uniprot.org/manual/init_met) | Cleavage of the initiator methionine |
| [Signal](http://www.uniprot.org/manual/signal) | Sequence targeting proteins to the secretory pathway or periplasmic space |
| [Transit peptide](http://www.uniprot.org/manual/transit) | Extent of a transit peptide for organelle targeting |
| [Propeptide](http://www.uniprot.org/manual/propep) | Part of a protein that is cleaved during maturation or activation |
| [Chain](http://www.uniprot.org/manual/chain) | Extent of a polypeptide chain in the mature protein |
| [Peptide](http://www.uniprot.org/manual/peptide) | Extent of an active peptide in the mature protein |
| **Regions** |
| [Topological domain](http://www.uniprot.org/manual/topo_dom) | Location of non-membrane regions of membrane-spanning proteins |
| [Transmembrane](http://www.uniprot.org/manual/transmem) | Extent of a membrane-spanning region |
| [Intramembrane](http://www.uniprot.org/manual/intramem) | Extent of a region located in a membrane without crossing it |
| [Domain](http://www.uniprot.org/manual/domain) | Position and type of each modular protein domain |
| [Repeat](http://www.uniprot.org/manual/repeat) | Positions of repeated sequence motifs or repeated domains |
| [Calcium binding](http://www.uniprot.org/manual/ca_bind) | Position(s) of calcium binding region(s) within the protein |
| [Zinc finger](http://www.uniprot.org/manual/zn_fing) | Position(s) and type(s) of zinc fingers within the protein |
| [DNA binding](http://www.uniprot.org/manual/dna_bind) | Position and type of a DNA-binding domain |
| [Nucleotide binding](http://www.uniprot.org/manual/np_bind) | Nucleotide phosphate binding region |
| [Region](http://www.uniprot.org/manual/region) | Region of interest in the sequence |
| [Coiled coil](http://www.uniprot.org/manual/coiled) | Positions of regions of coiled coil within the protein |
| [Motif](http://www.uniprot.org/manual/motif) | Short (up to 20 amino acids) sequence motif of biological interest |
| [Compositional bias](http://www.uniprot.org/manual/compbias) | Region of compositional bias in the protein |
| **Sites** |
| [Active site](http://www.uniprot.org/manual/act_site) | Amino acid(s) directly involved in the activity of an enzyme |
| [Metal binding](http://www.uniprot.org/manual/metal) | Binding site for a metal ion |
| [Binding site](http://www.uniprot.org/manual/binding) | Binding site for any chemical group (co-enzyme, prosthetic group, etc.) |
| [Site](http://www.uniprot.org/manual/site) | Any interesting single amino acid site on the sequence |
| **Amino acid modifications** |
| [Non-standard residue](http://www.uniprot.org/manual/non_std) | Occurence of non-standard amino acids (selenocysteine and pyrrolysine) in the protein sequence |
| [Modified residue](http://www.uniprot.org/manual/mod_res) | Modified residues excluding lipids, glycans and protein cross-links |
| [Lipidation](http://www.uniprot.org/manual/lipid) | Covalently attached lipid group(s) |
| [Glycosylation](http://www.uniprot.org/manual/carbohyd) | Covalently attached glycan group(s) |
| [Disulfide bond](http://www.uniprot.org/manual/disulfid) | Cysteine residues participating in disulfide bonds |
| [Cross-link](http://www.uniprot.org/manual/crosslnk) | Residues participating in covalent linkage(s) between proteins |
| **Natural variations** |
| [Alternative sequence](http://www.uniprot.org/manual/var_seq) | Amino acid change(s) producing alternate protein isoforms |
| [Natural variant](http://www.uniprot.org/manual/variant) | Description of a natural variant of the protein |
| **Experimental info** |
| [Mutagenesis](http://www.uniprot.org/manual/mutagen) | Site which has been experimentally altered by mutagenesis |
| [Sequence uncertainty](http://www.uniprot.org/manual/unsure) | Regions of uncertainty in the sequence |
| [Sequence conflict](http://www.uniprot.org/manual/conflict) | Description of sequence discrepancies of unknown origin |
| [Non-adjacent residues](http://www.uniprot.org/manual/non_cons) | Indicates that two residues in a sequence are not consecutive |
| [Non-terminal residue](http://www.uniprot.org/manual/non_ter) | The sequence is incomplete. Indicate that a residue is not the terminal residue of the complete protein |
| **Secondary structure** |
| [Helix](http://www.uniprot.org/manual/helix) | Helical regions within the experimentally determined protein structure |
| [Turn](http://www.uniprot.org/manual/turn) | Turns within the experimentally determined protein structure |
| [Beta strand](http://www.uniprot.org/manual/strand) | Beta strand regions within the experimentally determined protein structure |

The exact boundaries of the described sequence feature, as well as its length, are provided. When a feature is known to extend beyond the position that is given in this section, the endpoint specification will be preceded by '<' (less than) for features which continue to the N-terminal direction or by '>' (greater than) for features which continue to the C-terminal direction.

Example: [P62756](http://www.uniprot.org/uniprot/P62756#ptm%5Fprocessing)

Unknown endpoints are denoted by a question mark '?'.

Example: [P78586](http://www.uniprot.org/uniprot/P78586#ptm%5Fprocessing)

Uncertain endpoints are denoted by a question mark '?' before the position, e.g. '?42'.

Example: [Q3ZC31](http://www.uniprot.org/uniprot/Q3ZC31#ptm%5Fprocessing)

### Feature identifiers

Some features are associated with a unique and stable identifier that allows to construct links between these position-specific annotations and specialized protein-related databases.

The format of the identifiers is a 3-letter prefix, specific for an annotation type, separated by an underscore from a 6 to 10-digit number.

Feature identifiers currently exist for the following annotation topics: Propeptide, Chain, Peptide, Glycosylation, Alternative sequence and Natural variant.

|     |     |     |     |
| --- | --- | --- | --- |
| **Subsection** | **Identifier prefix** | **Availability** | **Example** |
| **Molecule processing** |
| [Propeptide](http://www.uniprot.org/manual/propep) | PRO | Any processed propeptide | [Q7XAD0](http://www.uniprot.org/uniprot/Q7XAD0#ptm_processing) |
| [Chain](http://www.uniprot.org/manual/chain)<br>[Peptide](http://www.uniprot.org/manual/peptide) | PRO | Any mature polypeptide | [Q9W568](http://www.uniprot.org/uniprot/Q9W568#ptm_processing)<br>[P15515](http://www.uniprot.org/uniprot/P15515#ptm_processing) |
| **Amino acid modifications** |
| [Glycosylation](http://www.uniprot.org/manual/carbohyd) | CAR | Only for residues attached to an oligosaccharide structure annotated in the [GlyConnect](https://glyconnect.expasy.org/) database | [P02771](http://www.uniprot.org/uniprot/P02771#ptm_processing) |
| **Natural variations** |
| [Alternative sequence](http://www.uniprot.org/manual/var_seq) | VSP | Any sequence with an ‘Alternative sequence’ feature | [P81278](http://www.uniprot.org/uniprot/P81278#sequences) |
| [Natural variant](http://www.uniprot.org/manual/variant) | VAR | Only for protein sequence variants of Hominidae (great apes and humans) | [P11171](http://www.uniprot.org/uniprot/P11171#sequences) |
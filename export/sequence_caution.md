---
title: Sequence caution
categories: Sequence,manual
---

This subsection of the 'Sequence' section reports difference(s) between the protein sequence shown in the UniProtKB entry and other available protein sequences derived from the same gene.

The sequence discrepancies described in this subsection are generally severe and thus distinct from those that are described in the ['Sequence conflict'](http://www.uniprot.org/manual/conflict) subsection. In this subsection, we list the differences between the [canonical sequence](http://www.uniprot.org/help/canonical%5Fand%5Fisoforms), displayed by default in the entry, and the sequence reported in the indicated reference (be it a paper, a submitted sequence or a prediction).

We annotate 6 different types of sequence discrepancies in this subsection:

- **Frameshift**: discrepancies are due to the insertion or deletion of one or more nucleotides in the underlying cDNA or genomic sequence relative to the canonical sequence.



Example: [O14467](http://www.uniprot.org/uniprot/O14467#sequences)
- **Erroneous initiation codon**: discrepancies are due to an erroneous initiation codon choice in the submitted sequence. The erroneous initiation codon may correspond to an internal codon and the sequence should be extended N-terminally. Conversely, the submitted sequence may be too long and has to be N-terminally shortened to match the canonical sequence.



Example: [Q7L2H7](http://www.uniprot.org/uniprot/Q7L2H7#sequences)
- **Erroneous termination codon**: the termination codon of the submitted sequence differs from that of the sequence displayed. A sequencing error introduced a stop codon, the sequence should be C-terminally extended by "translation" into a particular amino acid to match the canonical sequence. Conversely, the sequence may contain an amino acid instead of a bona fide termination signal. Finally, a stop codon should have been translated into a non-standard amino acid, either selenocysteine (Sec) or pyrrolysine (Pyl).



Example: [Q9Y6D0](http://www.uniprot.org/uniprot/Q9Y6D0#sequences)
- **Erroneous gene model prediction**: discrepancies are due to an erroneous gene model prediction. The predicted protein sequence (from the start to the stop codons and including all exon / intron boundaries) does not match the canonical sequence.



Example: [Q7XR80](http://www.uniprot.org/uniprot/Q7XR80#sequences)
- **Erroneous translation**: discrepancies are due to erroneous ORF assignement, or the CDS is thought to be in a different region of the mRNA, or a wrong genetic code has been used, etc.



Example: [Q96GX2](http://www.uniprot.org/uniprot/Q96GX2#sequences)
- **Miscellaneous discrepancy**: this category includes intron retention, chimeric DNA, unusual initiator codon (in eukaryotes), etc.



Examples: [P49762](http://www.uniprot.org/uniprot/P49762#sequences), [Q8TBF5](http://www.uniprot.org/uniprot/Q8TBF5#sequences)

Note that the cross-references linking to the problematic nucleotide sequences are tagged in the ['Cross-references'](http://www.uniprot.org/manual/cross%5Freferences%5Fsection) section (Sequence databases).
---
title: UniProtKB query fields
categories: Text_search,Technical,Website,help
---

Supported query fields for searching specific data in UniProtKB (see also [query syntax](http://www.uniprot.org/help/text-search) ).

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 31%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>accession</td>
<td><code>accession:P62988</code></td>
<td>Lists all entries with the primary or secondary <a href="http://www.uniprot.org/manual/accession_numbers">accession number</a> P62988.</td>
</tr>
<tr class="even">
<td>active</td>
<td><code>active:no</code></td>
<td>Lists all obsolete entries.</td>
</tr>
<tr class="odd">
<td>annotation</td>
<td><code>annotation:(type:non-positional)                         annotation:(type:positional)                         annotation:(type:mod_res "Pyrrolidone carboxylic acid" evidence:experimental)</code></td>
<td><p>Lists all entries with:</p>
<ul>
<li>any <a href="http://www.uniprot.org/help/general_annotation">general annotation (comments [CC])</a></li>
<li>any <a href="http://www.uniprot.org/help/sequence_annotation">sequence annotation (features [FT])</a></li>
<li>at least one amino acid modified with a Pyrrolidone carboxylic acid group</li>
</ul></td>
</tr>
<tr class="even">
<td>author</td>
<td><code>author:ashburner</code></td>
<td>Lists all entries with at least one reference co-authored by Michael Ashburner.</td>
</tr>
<tr class="odd">
<td>cdantigen</td>
<td><code>cdantigen:CD233</code></td>
<td>Lists all entries whose cluster of differentiation number is CD233 (see <a href="http://www.uniprot.org/docs/cdlist">cdlist.txt</a> ).</td>
</tr>
<tr class="even">
<td>chebi</td>
<td><code>chebi:18420</code></td>
<td>Lists all entries which are associated with the small molecule corresponding to ChEBI identifier 18420, Mg(2+) (see <a href="http://www.uniprot.org/help/chemical_data_search">How can I search UniProt for chemical or reaction data?</a> ).</td>
</tr>
<tr class="odd">
<td>citation</td>
<td><code>citation:("intracellular structural proteins")                         citation:(author:ashburner journal:nature)                   citation:9169874</code></td>
<td><p>Lists all entries with a <a href="http://www.uniprot.org/citations">literature citation</a> :</p>
<ul>
<li>containing the phrase "intracellular structural proteins" in either title or abstract</li>
<li>co-authored by Michael Ashburner and published in Nature</li>
<li>with the <a href="http://www.ncbi.nlm.nih.gov/pubmed">PubMed</a> identifier 9169874</li>
</ul></td>
</tr>
<tr class="even">
<td>cluster</td>
<td><code>cluster:(uniprot:A5YMT3 identity:0.9)</code></td>
<td>Lists all entries in the UniRef 90% identity cluster whose representative sequence is UniProtKB entry A5YMT3 ( <a href="http://www.uniprot.org/help/uniref">about UniRef</a> ).</td>
</tr>
<tr class="odd">
<td>count</td>
<td><code>annotation:(type:transmem count:5)                         annotation:(type:transmem count:[5 TO *])                         database:(type:pdb count:[20 TO *])</code></td>
<td><p>Lists all entries with:</p>
<ul>
<li>exactly 5 transmembrane regions</li>
<li>5 or more transmembrane regions</li>
<li>3 or more Cofactor comments</li>
<li>20 or more cross-references to PDB</li>
</ul></td>
</tr>
<tr class="even">
<td>created</td>
<td><code>created:[20121001 TO *]                         reviewed:yes AND created:[current TO *]</code></td>
<td>Lists all entries created since October 1st 2012.<br />
Lists all new UniProtKB/Swiss-Prot entries in the last release.</td>
</tr>
<tr class="odd">
<td>database</td>
<td><code>database:(type:pfam)                         database:(type:pdb 1aut)</code></td>
<td><p>Lists all entries with:</p>
<ul>
<li>a cross-reference to the Pfam database</li>
<li>a cross-reference to the PDB database entry 1aut</li>
</ul>
<p>(see <a href="http://www.uniprot.org/docs/dbxref">Databases cross-referenced in UniProtKB</a> and <a href="http://www.uniprot.org/help/mapping">Database mapping</a> )</p></td>
</tr>
<tr class="even">
<td>ec</td>
<td><code>ec:3.2.1.23</code></td>
<td>Lists all beta-galactosidases ( <a href="http://enzyme.expasy.org/">Enzyme nomenclature database</a> ).</td>
</tr>
<tr class="odd">
<td>evidence</td>
<td><code>annotation:(type:signal evidence:ECO_0000269)                         (type:mod_res phosphoserine evidence:ECO_0000269)                         annotation:(type:function AND evidence:ECO_0000255)</code></td>
<td><p>Lists all entries with:</p>
<ul>
<li>a signal sequence whose positions have been experimentally proven</li>
<li>experimentally proven phosphoserine sites</li>
<li>a function manually asserted according to rules</li>
</ul>
<p>(see <a href="http://www.uniprot.org/help/evidences">Evidence attribution</a> )</p></td>
</tr>
<tr class="even">
<td>existence</td>
<td><code>existence:"inferred from homology"</code></td>
<td>See <a href="http://www.uniprot.org/docs/pe_criteria">Protein existence criteria</a> .</td>
</tr>
<tr class="odd">
<td>family</td>
<td><code>family:serpin</code></td>
<td>Lists all entries belonging to the Serpin family of proteins ( <a href="http://www.uniprot.org/docs/similar">Index of protein domains and families</a> ).</td>
</tr>
<tr class="even">
<td>fragment</td>
<td><code>fragment:yes</code></td>
<td>Lists all entries with an incomplete sequence.</td>
</tr>
<tr class="odd">
<td>gene</td>
<td><code>gene:HPSE</code></td>
<td>Lists all entries for proteins encoded by gene HPSE, but also by HPSE2.</td>
</tr>
<tr class="even">
<td>gene_exact</td>
<td><code>gene_exact:HPSE</code></td>
<td>Lists all entries for proteins encoded by gene HPSE, but excluding variations like HPSE2 or HPSE_0.</td>
</tr>
<tr class="odd">
<td>goa</td>
<td><code>goa:(cytoskeleton)                         go:0015629</code></td>
<td><p>Lists all entries associated with:</p>
<ul>
<li>a GO term containing the word "cytoskeleton"</li>
<li>the GO term Actin cytoskeleton and any subclasses</li>
</ul></td>
</tr>
<tr class="even">
<td>host</td>
<td><code>host:mouse                         host:10090                         host:40674</code></td>
<td><p>Lists all entries for viruses infecting:</p>
<ul>
<li>organisms with a name containing the word "mouse" (including Arabidopsis thaliana (Mouse-ear cress)!)</li>
<li>Mus musculus (Mouse)</li>
<li>all mammals (all taxa classified under the taxonomy node for Mammalia)</li>
</ul></td>
</tr>
<tr class="odd">
<td>id</td>
<td><code>id:P00750</code></td>
<td>Returns the entry with the primary <a href="http://www.uniprot.org/manual/accession_numbers">accession number</a> P00750.</td>
</tr>
<tr class="even">
<td>inchikey</td>
<td><code>inchikey:WQZGKKKJIJFFOK-GASJEMHNSA-N</code></td>
<td>Returns entries associated with the small molecule identified by the <a href="https://en.wikipedia.org/wiki/International_Chemical_Identifier#InChIKey">InChIKey</a> WQZGKKKJIJFFOK-GASJEMHNSA-N, i.e. D-glucopyranose (see <a href="http://www.uniprot.org/help/chemical_data_search">How can I search UniProt for chemical or reaction data?</a> )</td>
</tr>
<tr class="odd">
<td>inn</td>
<td><code>inn:Anakinra</code></td>
<td>Lists all entries whose "International Nonproprietary Name" is Anakinra.</td>
</tr>
<tr class="even">
<td>interactor</td>
<td><code>interactor:P00520</code></td>
<td>Lists all entries describing interactions with the protein described by entry P00520.</td>
</tr>
<tr class="odd">
<td>keyword</td>
<td><code>keyword:toxin                         keyword:"Toxin [KW-0800]"</code></td>
<td>Lists all entries associated with a keyword matching "Toxin" in its name or description ( <a href="http://www.uniprot.org/keywords">UniProtKB Keywords</a> ). Lists all entries associated with the UniProtKB keyword <a href="http://www.uniprot.org/keywords/KW-0800">Toxin</a> .</td>
</tr>
<tr class="even">
<td>length</td>
<td><code>length:[500 TO 700]</code></td>
<td>Lists all entries describing sequences of length between 500 and 700 residues.</td>
</tr>
<tr class="odd">
<td>lineage</td>
<td></td>
<td>This field is a synonym for the field <code>taxonomy</code> .</td>
</tr>
<tr class="even">
<td>mass</td>
<td><code>mass:[500000 TO *]</code></td>
<td>Lists all entries describing sequences with a mass of at least 500,000 Da.</td>
</tr>
<tr class="odd">
<td>method</td>
<td><code>method:maldi                         method:xray</code></td>
<td>Lists all entries for proteins identified by: matrix-assisted laser desorption/ionization (MALDI), crystallography (X-Ray). The <code>method</code> field searches names of physico-chemical identification methods in the <a href="http://www.uniprot.org/help/biophysicochemical_properties">'Biophysicochemical properties' subsection</a> of the <a href="http://www.uniprot.org/help/function_section">'Function' section</a> , the 'Publications' and 'Cross-references' sections.</td>
</tr>
<tr class="even">
<td>mnemonic</td>
<td><code>mnemonic:ATP6_HUMAN</code></td>
<td>Lists all entries with entry name (ID) ATP6_HUMAN. Searches also obsolete entry names ( <a href="http://www.uniprot.org/help/difference_accession_entryname">What is the difference between an accession number (AC) and the entry name?</a> ).</td>
</tr>
<tr class="odd">
<td>modified</td>
<td><code>modified:[20120101 TO 20120301]                         reviewed:yes AND modified:[current TO *]</code></td>
<td>Lists all entries that were last modified between January and March 2012.<br />
Lists all UniProtKB/Swiss-Prot entries modified in the last release.</td>
</tr>
<tr class="even">
<td>annotation:(type:mutagen)</td>
<td><code>annotation:(type:mutagen)                         annotation:(type:mutagen phosphorylation)</code></td>
<td>Lists all entries that have annotations about the effect of an "experimental mutation":/help/mutagen on the biological properties of the protein.<br />
Lists all entries with annotated experimental mutations affecting phosphorylation.</td>
</tr>
<tr class="odd">
<td>name</td>
<td><code>name:"prion protein"</code></td>
<td>Lists all entries for prion proteins.</td>
</tr>
<tr class="even">
<td>organelle</td>
<td><code>organelle:Mitochondrion</code></td>
<td>Lists all entries for proteins encoded by a gene of the mitochondrial chromosome.</td>
</tr>
<tr class="odd">
<td>organism</td>
<td><code>organism:"Ovis aries"                         organism:9940                         organism:sheep</code></td>
<td>Lists all entries for proteins expressed in sheep (first 2 examples) and organisms whose name contains the term "sheep" ( <a href="http://www.uniprot.org/taxonomy">UniProt taxonomy</a> ).</td>
</tr>
<tr class="even">
<td>plasmid</td>
<td><code>plasmid:ColE1</code></td>
<td>Lists all entries for proteins encoded by a gene of plasmid ColE1 ( <a href="http://www.uniprot.org/docs/plasmid">Controlled vocabulary of plasmids</a> ).</td>
</tr>
<tr class="odd">
<td>proteome</td>
<td><code>proteome:UP000005640</code></td>
<td>Lists all entries from the human <a href="http://www.uniprot.org/proteomes">proteome</a> .</td>
</tr>
<tr class="even">
<td>proteomecomponent</td>
<td><code>proteomecomponent:"chromosome 1" and organism:9606</code></td>
<td>Lists all entries from the human chromosome 1.</td>
</tr>
<tr class="odd">
<td>replaces</td>
<td><code>replaces:P02023</code></td>
<td>Lists all entries that were created from a merge with entry P02023 ( <a href="http://www.uniprot.org/faq/6">see FAQ</a> ).</td>
</tr>
<tr class="even">
<td>reviewed</td>
<td><code>reviewed:yes</code></td>
<td>Lists all UniProtKB/Swiss-Prot entries ( <a href="http://www.uniprot.org/help/uniprotkb">about UniProtKB</a> ).</td>
</tr>
<tr class="odd">
<td>scope</td>
<td><code>scope:mutagenesis</code></td>
<td>Lists all entries containing a reference that was used to gather information about mutagenesis (Entry view: "Cited for", <a href="http://www.uniprot.org/manual/references">See 'Publications' section of the user manual</a> ).</td>
</tr>
<tr class="even">
<td>sequence</td>
<td><code>sequence:P05067-9</code></td>
<td>Lists all entries containing a link to isoform 9 of the sequence described in entry P05067. Allows searching by specific sequence identifier.</td>
</tr>
<tr class="odd">
<td>sequence_modified</td>
<td><code>sequence_modified:[20120101 TO 20120301]                         reviewed:yes AND sequence_modified:[current TO *]</code></td>
<td>Lists all entries whose sequences were last modified between January and March 2012.<br />
Lists all UniProtKB/Swiss-Prot entries whose sequences were modified in the last release.</td>
</tr>
<tr class="even">
<td>strain</td>
<td><code>strain:wistar</code></td>
<td>Lists all entries containing a reference relevant to strain wistar ( <a href="http://www.uniprot.org/docs/strains">Lists of strains in reference comments</a> and <a href="http://www.uniprot.org/help/taxonomy#strain">Taxonomy help: organism strains</a> ).</td>
</tr>
<tr class="odd">
<td>taxonomy</td>
<td><code>taxonomy:40674</code></td>
<td>Lists all entries for proteins expressed in <a href="http://www.uniprot.org/taxonomy/40674">Mammals</a> . This field is used to retrieve entries for all organisms classified below a given taxonomic node ( <a href="http://www.uniprot.org/help/taxonomy#lineage">taxonomy classification</a> ).</td>
</tr>
<tr class="even">
<td>tissue</td>
<td><code>tissue:liver</code></td>
<td>Lists all entries containing a reference describing the protein sequence obtained from a clone isolated from liver ( <a href="http://www.uniprot.org/docs/tisslist">Controlled vocabulary of tissues</a> ).</td>
</tr>
<tr class="odd">
<td>annotation:(type:variant)</td>
<td><code>annotation:(type:variant)                         annotation:(type:variant dkca2)</code></td>
<td>Lists all entries that document "natural variants":/help/variant of the protein sequence.<br />
Lists all entries with variants annotated in the context of the disease "Dyskeratosis congenita, autosomal dominant, 2 (DKCA2)":https://www.uniprot.org/diseases/DI-00407</td>
</tr>
<tr class="even">
<td>web</td>
<td><code>web:wikipedia</code></td>
<td>Lists all entries for proteins that are described in <a href="http://wikipedia.org/">Wikipedia</a> .</td>
</tr>
</tbody>
</table>
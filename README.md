# Motif

### Table of Contents

[Multiple sequence alignments](https://github.com/ToshkaDev/Motif#multiple-sequence-alignments)

* [The RefSeq alignment](https://github.com/ToshkaDev/Motif#the-refseq-alignment)
* [The Uniprot alignment](https://github.com/ToshkaDev/Motif#the-uniprot-alignment)
* [The GTDB alignment](https://github.com/ToshkaDev/Motif#the-gtdb-alignment)
* [Eukaryotic alignment](https://github.com/ToshkaDev/Motif#eukaryotic-alignment)

[Phylogenetic trees of Eukaryotic dCache_1AA proteins](https://github.com/ToshkaDev/Motif#phylogenetic-trees-of-eukaryotic-dcache_1aa-proteins)

[Structures, models, and molecular docking](https://github.com/ToshkaDev/Motif#structures-models-and-molecular-docking)

* [Modeled structures of prokaryotic dCache_1AA domain protein sensors ](https://github.com/ToshkaDev/Motif#modeled-structures-of-prokaryotic-dcache_1aa-domain-protein-sensors)
* [Structures of eukaryotic dCache_1AA proteins docked with ligands](https://github.com/ToshkaDev/Motif#structures-of-eukaryotic-dcache_1aa-proteins-docked-with-ligands)

-----------
We have discovered a universal amino acid binding motif (AA_motif) present in dCache_1 domain (http://pfam.xfam.org/family/PF02743) containing proteins throughout the Tree of Life (link to the paper: https://www.pnas.org/doi/10.1073/pnas.2110415119). 
The motif in its canonical form has the following definition: 

Y....R.WY{n1}Y{n2}D.

Studying variability of the motif positions in experimentally studied organisms that still permits amino acid binding we deduced the following generalized motif definition:

[YFWL]....[RK].W[WYF]{n1}[YF]{n2}[D].

In these expressions any amino acid inside the given brackets can be present in the corresponding position, n1 - a varying distance of approximately 13-17 amino acid residues, n2 - a varying distance of approximately 27-34 residues. 

As we have established, two dCache_1 domains are present in eukaryotic proteins that have the motif. In alpha2/delta-1 subunits of Voltage gated calcium channels and in their homologs the motif is present in the dCache_1 domain with the VWA insertion that splits the motif in two parts, and, correspondingly, n1 in the above expression is a varying distance of approximately 215-245 amino acid residues. In CACHD1 proteins and in their homologs the motif is present in the second dCache_1 domain that does not have the VWA insertion and, correspondengly, the distance is within the regular range of 27-34 residues.

## Multiple sequence alignments
Using the generalized universal amino acid binding motif (AA_motif) definition we scanned three protein sequence databases: GTDB (representative dataset; https://gtdb.ecogenomic.org/), NCBI RefSeq (https://www.ncbi.nlm.nih.gov/refseq/), and Uniprot (https://www.uniprot.org/). The details of this procedure can be found in Materials and Methods section of the paper describing the discovery of the motif throughout the Tree of Life.

Extracting regions corresponding to the dCache_1 domains in the identified protein sequences containing the AA_motif we constructed multiple sequence alignments (MSAs).

### The RefSeq alignment
The RefSeq alignment is in **RefSeq** folder. There are **32395** dCache_1 domain containing proteins in the RefSeq database that have the amino acid binding motif.

Positions corresponding to the motif in this MSA:

Y(**2091**)....R(**2302**).W(**2385**)Y(**2414**){n1}Y(**2727**){n2}D(**3326**)

### The Uniprot alignment
The Uniprot alignment is in **Uniprot** folder. There are **11330** dCache_1 domain containing proteins in the Uniprot database that have the amino acid binding motif.

Positions corresponding to the motif in this MSA:

Y(**308**)....R(**313**).W(**315**)Y(**316**){n1}Y(**345**){n2}D(**420**)

### The GTDB alignment
The GTDB alignment is in **GTDB_Representative_Set** folder. There are **10700** bacterial and **114** archaeal dCache_1 domain containing proteins in the GTDB database that have the universal amino acid binding motif.

Positions corresponding to the motif in the bacterial proteins MSA:
 
Y(**1160**)....R(**1278**).W(**1290**)Y(**1291**){n1}Y(**1431**){n2}D(**1647**)

Positions corresponding to the motif in the archaeal proteins MSA:

Y(**163**)....R(**168**).W(**170**)Y(**171**){n1}Y(**189**){n2}D(**219**)

### Eukaryotic alignment

Multiple sequence alignments of eukaryotic protein sequences of dCache_1 domains with the AA_motif is in **Eukaryotes** folder.

As eukaryotic alpha-2/delta-1 and CACHD1 proteins comprised of two dCache_1 domains, one of which has the VWA insertion (see the paper describing the universal AA_motif for details), and the number of sequenced eukaryotic genomes is limited, several databases (NCBI RefSeq, NCBI NR, Uniprot, 1KP, and EukProt) have been scanned to identify and extract homologous proteins. We have verified the presence of the motif constructing MSAs including in the alignment already identified motif-containing eukaryotic and bacterial sequences.

MSA of double dCache_1AA proten sequences from the representative set of eukaryotic organisms (file *Eukaryotes_double_dCache_1_aln.fa*).
Positions corresponding to the motif in the **first** dCache_1 domain (in those proteins, in which the motif is preserved):

Y(**295**)....R(**300**).W(**302**)Y(**303**){n1}Y(**648**){n2}D(**715**)

Positions corresponding to the motif in the **second** dCache_1 domain (in those proteins, in which the motif is preserved):

Y(**1231**)....R(**1236**).W(**1242**)Y(**1243**){n1}Y(**1265**){n2}D(**1363**)

MSA of all dCache_1AA proten sequences from the complete set of eukaryotic organisms (zip archive *Eukaryotic_proteins_Complete_set_aln.fa.zip*):
Positions corresponding to the motif in the **first** dCache_1 domain (in those proteins, in which the motif is preserved):

Y(**8986**)....R(**8999**).W(**9001**)Y(**9002**){n1}Y(**11639**){n2}D(**12545**)

Positions corresponding to the motif in the **second** dCache_1 domain (in those proteins, in which the motif is preserved):

Y(**16149**)....R(**16226**).W(**16228**)Y(**16229**){n1}Y(**16362**){n2}D(**17717**)


## Phylogenetic trees of Eukaryotic dCache_1AA proteins 

The trees are located in **Eukaryotes** folder. There are two trees in the folder: (i) inferred using maximum likelihood estimation implemented in RaXML in Newick format (file *Eukaryotes_double_dCache_1_RaXML_tree.newick*) and (ii) inferred using Bayesian inference implemented in MrBayes in Nexus format (file *Eukaryotes_double_dcache_1_MrBayes_tree.tre*).

## Structures, models, and molecular docking

### Modeled structures of prokaryotic dCache_1AA domain protein sensors 

Structures of dCache_1AA domain protein sensors from various phyla of Archaea and Bacteria were modeled by Phyre2 and are located in RefSeq folder (zip archive *Structures_modeled_by_Phyre2.zip*).

### Structures of eukaryotic dCache_1AA proteins docked with ligands

Structures of alpha2/delta-1 and CACHD1 are located in Eukaryotes/Structures_Autodock folder. 

The list of files in the folder:

1. File 1. *Rabbit_alpha2delta1_docked_with_ligands.pdb*

A cryo-EM structure was used for docking experiments.
 
2. File 2. *Fly_alpha2delta1_docked_with_ligands.pdb*

An AlphaFold model was used for docking experiments.

3. File 3. *Human_CACHD1_docked_with_ligands.pdb*

An AlphaFold model was used for docking experiments.

4. File 4. *Fly_CACHD1_docked_with_ligands.pdb*

An AlphaFold model was used for docking experiments.





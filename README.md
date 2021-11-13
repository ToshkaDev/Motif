# Motif

We have discovered a universal amino acid binding motif present in dCache_1 domain (http://pfam.xfam.org/family/PF02743) containing proteins throughout the Tree of Life (link to the paper: https://doi.org/10.1101/2021.05.05.442820). 
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
The RefSeq alignment is in **RefSeq** folder. There are **32395** dCache_1 domain containing proteins in the RefSeq database that have the universal amino acid binding motif.

Positions corresponding to the motif in this MSA:
Y(**2091**)....R(**2302**).W(**2385**)Y(**2414**){n1}Y(**2727**){n2}D(**3326**)

### The Uniprot alignment
The Uniprot alignment is in **Uniprot** folder. There are **11330** dCache_1 domain containing proteins in the Uniprot database that have the universal amino acid binding motif.

Positions corresponding to the motif in this MSA:
Y(**308**)....R(**313**).W(**315**)Y(**316**){n1}Y(**345**){n2}D(**420**)

### The GTDB alignment
The GTDB alignment is in **GTDB_Representative_Set** folder. There are **10700** bacterial and **114** archaeal dCache_1 domain containing proteins in the GTDB database that have the universal amino acid binding motif.

Positions corresponding to the motif in the bacterial proteins MSA: 
Y(**1160**)....R(**1278**).W(**1290**)Y(**1291**){n1}Y(**1431**){n2}D(**1647**)

Positions corresponding to the motif in the archaeal proteins MSA:
Y(**163**)....R(**168**).W(**170**)Y(**171**){n1}Y(**189**){n2}D(**219**)

### Eukaryotic alignment

The MSA of eukaryotic protein sequences of dCache_1 domains with the AA_motif is in **Eukaryotes** folder. In this folder a Maximum-likelihood tree built using the eukaryotic protein sequences of dCache_1 domains containing the AA_motif can also be found.

As eukaryotic alpha-2/delta-1 and CACHD1 proteins have double dCache_1 domains, one of which has the VWA insertion (see the paper describing the universal AA_motif for details), and the number of sequenced eukaryotic genomes is limited, several databases have been scanned to identify and extract homologous proteins. Using several eukaryotic and bacterial dCache_1 containing protein sequences as queries we searched in proteoms of our compiled set of representative eukaryotic organisms. We scanned the NCBI Nonredundant database, Uniprot, and 1KP, collected the identified protein sequences and verified the presence of the motif constructing MSAs including in the alignment already identified motif-containing eukaryotic and bacterial sequences.

Positions corresponding to the motif in the **first** dCache_1 domain in the MSA of eukayotic proteins (in those proteins, in which the motif is preserved):
Y(**415**)....R(**420**).W(**422**)Y(**423**){n1}Y(**846**){n2}D(**970**)

Positions corresponding to the motif in the **second** dCache_1 domain in the MSA of eukayotic proteins (in those proteins, in which the motif is preserved):
Y(**1690**)....R(**1696**).W(**1698**)Y(**1699**){n1}Y(**1724**){n2}D(**1866**)

### Phylogenetic trees of Eukaryotic dCache_1AA proteins are located in Eukaryotes folder. 

There are two trees in the folder: (i) inferred using maximum likelihood estimation implemented in RaXML and (ii) inferred using Bayesian inference implemented in MrBayes.

## Structures, models, and molecular docking

### Modeled structures of prokaryotic dCache_1AA domain protein sensors 

Structures of dCache_1AA domain protein sensors from various phyla of Archaea and Bacteria were modeled by Phyre2 and are located in RefSeq folder (zip archive 'Structures_modeled_by_Phyre2.zip').

### Structures of eukaryotic dCache_1AA proteins docked with ligands.

Structures of alpha2/delta-1 and CACHD1 are located in Eukaryotes/Structures_Autodock folder. 

The list of files in the folder:

1. File 1. Rabbit_alpha2delta1_docked_with_ligands.pdb   Cryo-EM structure was used for docking experiments. 
2. File 2. Fly_alpha2delta1_docked_with_ligands.pdb      AlphaFold model was used for docking experiments.
3. File 3. Human_CACHD1_docked_with_ligands.pdb          AlphaFold model was used for docking experiments.
4. File 4. Fly_CACHD1_docked_with_ligands.pdb            AlphaFold model was used for docking experiments.

*V. M. Gumerov, E. P. Andrianova, M. A. Matilla, Karen M. Page, Elizabet Monteagudo-Cascales, A. C. Dolphin, T. Krell, I. B. Zhulin (2020). Amino acid sensor conserved from bacteria to humans. https://doi.org/10.1101/2021.05.05.442820*
























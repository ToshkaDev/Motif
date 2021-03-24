# Motif

We discovered a universal amino acid binding motif present in dCache_1 domain (http://pfam.xfam.org/family/PF02743) containing proteins throughout the Tree of Life. 
The motif in its canonical form has the following definition: 

Y....R.WY{n1}Y{n2}D.

Studying variability of the motif positions in experimentally studied organisms that still permits amino acid binding we deduced the following generalised motif definition:

[YFWL]....[RK].W[WYF]{n1}[YF]{n2}[D].

In these expressions brackets mean that any amino acid inside the given brackets can be present in the corresponding position, n1 - a varying distance of approximately 14-17 amino acid residues, n2 - a varying distance of approximately 28-34 residues. In eukariotic dCache_1 containing proteins with the VWA domain insertion n1 is a varying distance of approximately 215-245 amino acid residues. 

## Multiple sequence alignments
Using the generalised universal amino acid binding motif definition we scanned three protein sequence databases: GTDB (representative dataset; https://gtdb.ecogenomic.org/), NCBI RefSeq (https://www.ncbi.nlm.nih.gov/refseq/), and Uniprot (https://www.uniprot.org/). The details of this procedure can be found in Materials and Methods section of the paper describing the discovery of the motif throughout the Tree of Life.

Extracting regions corresponding to the dCache_1 domains in the identified protein sequences we constructed multiple sequence alignemnts.

### The RefSeq alignment
The RefSeq alignment is in RefSeq folder. There are **35433** dCache_1 domain containing proteins in the RefSeq database that have the universal amino acid binding motif.

Positions corresponding to the motif in this alignment:
Y(**2103**)....R(**2320**).W(**2405**)Y(**2434**){n1}Y(**2756**){n2}D(**3376**)

### The Uniprot alignment
The Uniprot alignment is in Uniprot folder. There are **12522** dCache_1 domain containing proteins in the Uniprot database that have the universal amino acid binding motif.

Positions corresponding to the motif in this alignment:
Y(**310**)....R(**315**).W(**317**)Y(**318**){n1}Y(**352**){n2}D(**424**)

### The GTDB alignment
The GTDB alignment is in GTDB_Representative_Set folder. There are **11453** bacterial and **114** archaeal dCache_1 domain containing proteins in the GTDB database that have the universal amino acid binding motif.

Positions corresponding to the motif in bacterial proteins alignment: 
Y(**1168**)....R(**1287**).W(**1299**)Y(**1300**){n1}Y(**1443**){n2}D(**1660**)

Positions corresponding to the motif in archaeal proteins alignment:
Y(**163**)....R(**168**).W(**170**)Y(**171**){n1}Y(**190**){n2}D(**219**)

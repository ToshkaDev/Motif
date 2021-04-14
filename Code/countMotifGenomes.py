#!/usr/bin/python

from Bio import SeqIO
import sys


'''The script process an alignment extracting sequnces containg a specific motif. 
#Input:
#>GCA_000730285.1_CP007174.1_2103
#---------------------------------HDLANLVSNEISHVQSVSQMLSKSPPIQGGDFEKA----
#-------------------------------------------KETLNQAEDSSGRIV---DFYMWLDKDG-
#>GCF_000698785.1_NZ_CP007536.1_742
#-----------------------------------LANLVSSEISHVQSVLQMLSKSPLIQDGDFEKA----
#-------------------------------------------KETLNQAEDSTSEIV---DFYMWLDRDG-
#Output is a file of protein ids and motif variant:
#GCA_001509375.1		Y....R.WY{n1}Y{n2}D
#GCA_002502785.1		Y....R.WY{n1}Y{n2}D
#GCA_013329455.1		Y....R.WY{n1}Y{n2}D
'''


INPUT_FILE = sys.argv[1]
#output file with a list of genomes and motifs
OUPTU_FILE = sys.argv[2]

#Options:
# 'count' - count motif variuants
# 'fasta' - extract proteins that have the motif in the specified position in 'fasta' format.
MODE = sys.argv[3]

#Y....R.WY{n1}Y{n2}D
POS1_AROMATIC_ALIPH = set(["W","F","Y","L"])
POS2_POLAR_POSITIVE = set(["R","K"])
POS3_AROMATIC = set(["W"])
POS4_AROMATIC = set(["W","F","Y"])
POS5_AROMATIC = set(["Y", "F"])
#POS6_POLAR_NEGATIVE = set(["D"])
POS6_POLAR_NEGATIVE = set(["N","D"])


# GTDB
#Bacteria:
#Y_Position = 1260
#R_Position = 1390
#W_Position = 1402
#Y2_Position = 1403
#Y3_Position = 1559
#D_Position = 1786

#Archaea:
#~ Y_Position = 171
#~ R_Position = 176
#~ W_Position = 178
#~ Y2_Position = 179
#~ Y3_Position = 197
#~ D_Position = 237

#Pfam Uniprot full alignment:
#~ Y_Position = 441
#~ R_Position = 457
#~ W_Position = 464
#~ Y2_Position = 466
#~ Y3_Position = 538
#~ D_Position = 682


#RefSeq alignment
Y_Position = 3371
R_Position = 3688
W_Position = 3804
Y2_Position = 3850
Y3_Position = 4486
D_Position = 5912



assmeblies_with_motif = []

def process():
	with open(INPUT_FILE, "r") as inputFile, open(OUPTU_FILE, "w") as outputFile:
		if MODE == "count":
			for record in SeqIO.parse(inputFile, "fasta"):
				protSequnce = str(record.seq)
				if protSequnce[Y_Position] in POS1_AROMATIC_ALIPH and protSequnce[R_Position] in POS2_POLAR_POSITIVE and protSequnce[W_Position] in POS3_AROMATIC \
					and protSequnce[Y2_Position] in POS4_AROMATIC and protSequnce[Y3_Position] in POS5_AROMATIC and protSequnce[D_Position] in POS6_POLAR_NEGATIVE:
						genomeAssembly = "_".join(record.description.split("_")[0:2])
						motif = "".join([protSequnce[Y_Position], "....", protSequnce[R_Position], ".", protSequnce[W_Position], protSequnce[Y2_Position], "{n1}", protSequnce[Y3_Position], "{n2}", protSequnce[D_Position]])
						outputFile.write(genomeAssembly + "\t\t" + motif + "\n")
		elif MODE == "fasta":
			for record in SeqIO.parse(inputFile, "fasta"):
				protSequnce = str(record.seq)
				if protSequnce[Y_Position] in POS1_AROMATIC_ALIPH and protSequnce[R_Position] in POS2_POLAR_POSITIVE and protSequnce[W_Position] in POS3_AROMATIC \
					and protSequnce[Y2_Position] in POS4_AROMATIC and protSequnce[Y3_Position] in POS5_AROMATIC and protSequnce[D_Position] in POS6_POLAR_NEGATIVE:
						outputFile.write(">" + record.description + "\n")	
						outputFile.write(protSequnce + "\n")	
					


process()








#!/usr/bin/python
import os
import collections


AAs = set(["alanine", "arginine", "asparagine", "aspartate", "cysteine", "glutamine", "glycine", "leucine", "lysine", \
"methionine", "phenylalanine", "isoleucine", "histidine", "serine", "threonine", "tyrosine", "valine", "tryptophan", \
"glutamate", "proline"])

RECEPTOR_TO_LIGANDS = collections.defaultdict(list)


#This routine is used to write down first non-amino acids and then amino acids
def recordLigands(ligandsAndAffins, outputFile, indx):
	aaLigands = []
	for ligandAndAffin in ligandsAndAffins:
		#First write down non-amino acids
		if ligandAndAffin[0] not in AAs:
			outputFile.write("\t" + ligandAndAffin[indx])
		#Collecting amino acids here for the later recording
		else:
			aaLigands.append(ligandAndAffin)
	for ligAndAff in aaLigands:
		 outputFile.write("\t" + ligAndAff[indx])

tempSet = set()
for sysObject in os.listdir("."):
	if os.path.isdir(sysObject):
		os.chdir(sysObject)
		for sysObject2 in os.listdir("."):
			if os.path.isdir(sysObject2):
				receptorName = sysObject2
				os.chdir(sysObject2)
				for sysObject3 in os.listdir("."):
					if os.path.isfile(sysObject3) and len(sysObject3.split("_")) > 1 and sysObject3.split("_")[1] == "log.txt":
						print os.getcwd()
						ligandName = sysObject3.split("_")[0]
						with open (sysObject3) as inputFile:
							bindingAffinityLine = inputFile.readlines()[26]
						bindingAffinity = bindingAffinityLine.split(" ")[12]
						tempSet.add(bindingAffinity)
						RECEPTOR_TO_LIGANDS[receptorName].append((ligandName, bindingAffinity))
				
				os.chdir("..")
		os.chdir("..")
print tempSet

with open ("AutodockFolders_Summary2", "w") as outputFile:
	#Write down headers (ligand names)
	for receptor, ligandsAndAffins in RECEPTOR_TO_LIGANDS.items():
		outputFile.write("*****************")
		recordLigands(ligandsAndAffins, outputFile, 0)	
		break
	#Write down receptors and ligand affinities 
	receptors = sorted(RECEPTOR_TO_LIGANDS.keys())
	for receptor in receptors:
		ligandsAndAffins = RECEPTOR_TO_LIGANDS[receptor]
	#for receptor, ligandsAndAffins in RECEPTOR_TO_LIGANDS.items():
		outputFile.write("\n" + receptor)
		recordLigands(ligandsAndAffins, outputFile, 1)			
					
			
			
			
			
			
			
			
							

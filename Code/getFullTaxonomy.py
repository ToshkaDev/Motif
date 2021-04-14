#!/usr/bin/python
import sys, getopt
import collections
from ete2 import NCBITaxa
import os
import re

# Update NCBI taxonomy database if needed
#ncbi = NCBITaxa()
# ncbi.update_taxonomy_database()

USAGE = "\n\n The script extracts full taxonomy information \n\n" + \
	"python 	" + sys.argv[0] + '''
	-h || --help               - help
	-i || --ifile              - input file with organism names. Input files is expected to be a
		                       file with organism names not from GDTB, but from NCBI
	-o || --ofile              - output file with full taxonomy informtion
	-s || --source             - taxonomy source to use to extract the information from: currently 'GTDB' or 'NCBI'
	-r || --replace            - replace underscores with spaces or not in organism names: 'yes' or 'no'; dafult is "no"
	'''
	
INPUT_FILE = None
OUTPUT_FILE = None
# Currently: NCBI or GTDB
TAXONOMY_SOURCE = "NCBI"
REMOVE_DASHES = False
NCBI_GENUS_TO_FULL_TAXONOMY = collections.defaultdict(list)
GTDB_GENUS_TO_FULL_TAXONOMY = collections.defaultdict(list)

ORGANISM_NAME_TO_AMMOUNT = collections.defaultdict(int)
ORGANISM_NAME_TO_ORIGINAL_NAME = {}
ORGANISM_NAMES_LIST = []
#GTDB_TAXONOMY_FILE = "/".join(os.path.realpath(__file__).split("/")[:-1]) + "/ar122_bac120_metadata_r89_taxonomy.tsv"
GTDB_TAXONOMY_FILE = "/".join(os.path.realpath(__file__).split("/")[:-1]) + "/ar122_bac120_metadata_r95_taxonomy.tsv"
	
def initialize(argv):
	global INPUT_FILE, OUTPUT_FILE, TAXONOMY_SOURCE, REMOVE_DASHES
	try:
		opts, args = getopt.getopt(argv[1:],"hi:o:s:r:",["help", "ifile=", "ofile=", "source=", "remove="])
		if len(opts) == 0:
			raise getopt.GetoptError("Options are required\n")
	except getopt.GetoptError as e:
		print "===========ERROR==========\n " + str(e) + USAGE
		sys.exit(2)
	try:
		for opt, arg in opts:
			if opt in ("-h", "--help"):
				print USAGE
				sys.exit()
			elif opt in ("-i", "--ifile"):
				INPUT_FILE = str(arg).strip()
			elif opt in ("-o", "--ofile"):
				OUTPUT_FILE = str(arg).strip()
			elif opt in ("-s", "--source"):
				TAXONOMY_SOURCE = str(arg).strip()
			elif opt in ("-r", "--remove"):
				val = str(arg).strip()
				if val == "yes":
					REMOVE_DASHES = True
	except Exception as e:
		print "===========ERROR==========\n " + str(e) + USAGE
		sys.exit(2)
	initializeDataStructures()
			
def initializeDataStructures():
	with open(INPUT_FILE, "r") as inputFile:
		for name in inputFile:
			organismName = name.strip()
			if len(organismName):
				if REMOVE_DASHES:
					organismName = " ".join(organismName.split("_"))
				if TAXONOMY_SOURCE == "NCBI":
					ORGANISM_NAMES_LIST.append(organismName)
				elif TAXONOMY_SOURCE == "GTDB":
					ORGANISM_NAME_TO_AMMOUNT[organismName.lower()] += 1
					ORGANISM_NAME_TO_ORIGINAL_NAME[organismName.lower()] = organismName		


def getNcbiTaxonomy():
	ncbi = NCBITaxa()	
	nameToTaxIdList = ncbi.get_name_translator(ORGANISM_NAMES_LIST)
        #print (str(nameToTaxIdList))
	with open (OUTPUT_FILE, "w") as outputFile:
		for name in ORGANISM_NAMES_LIST:
		#for name, taxIds in nameToTaxIdList.items():
			taxIds = nameToTaxIdList[name]
			for eachId in taxIds:
				lineage = ncbi.get_lineage(str(eachId))
				names = ncbi.get_taxid_translator(lineage)
				outputFile.write("\t".join([names[taxid] for taxid in lineage]) + "\n")

def getGTDBTaxonomy():
	with open(GTDB_TAXONOMY_FILE, "r") as gtdbTaxonomyFile, open (OUTPUT_FILE, "w") as outputFile:
		for line in gtdbTaxonomyFile:
			line = line.split("\t")
			gtdbTaxonomy = line[1]
			ncbiTaxonomy = line[2]			
			ncbiGenusLower = getTaxonomyLevel(ncbiTaxonomy, "g__").lower()
			gtdbGenusLower = getTaxonomyLevel(gtdbTaxonomy, "g__").lower()
			NCBI_GENUS_TO_FULL_TAXONOMY[ncbiGenusLower].append(gtdbTaxonomy)
			GTDB_GENUS_TO_FULL_TAXONOMY[gtdbGenusLower].append(gtdbTaxonomy)
			
			ncbiNameLower = getTaxonomyLevel(ncbiTaxonomy, "s__").lower()
			gtdbNameLower = getTaxonomyLevel(gtdbTaxonomy, "s__").lower()
			ncbiNameLower = re.sub("^.__", "", ncbiNameLower)
			gtdbNameLower = re.sub("^.__", "", gtdbNameLower)
			if ncbiNameLower in ORGANISM_NAME_TO_AMMOUNT:
				saveGDTBTaxonomy(ncbiNameLower, gtdbTaxonomy, outputFile)
			elif gtdbNameLower in ORGANISM_NAME_TO_AMMOUNT:
				saveGDTBTaxonomy(gtdbNameLower, gtdbTaxonomy, outputFile)
		processNotFoundOrganisms(outputFile)


def getTaxonomyLevel(taxonomy, prefix):
	if prefix != "s__":
		taxStart = taxonomy.find(prefix) + 3
		taxEnd = taxonomy.find(";", taxStart)
		return taxonomy[taxStart:taxEnd].strip()
	return taxonomy.split(";")[-1].strip()
	

def processNotFoundOrganisms(outputFile):
	# print organisms for which retrieving of taxonomy was not successfull
	organismNameToAmmount = ORGANISM_NAME_TO_AMMOUNT.copy()	
	for organism in organismNameToAmmount:
		organismGenus = organism.split(" ")[0]
		if organismGenus in NCBI_GENUS_TO_FULL_TAXONOMY:
			saveGDTBTaxonomy(organism, NCBI_GENUS_TO_FULL_TAXONOMY[organismGenus][0], outputFile, True)
		elif organismGenus in GTDB_GENUS_TO_FULL_TAXONOMY:
			saveGDTBTaxonomy(organism, GTDB_GENUS_TO_FULL_TAXONOMY[organismGenus][0], outputFile, True)
			 	 
	for organism in ORGANISM_NAME_TO_AMMOUNT:
		outputFile.write(ORGANISM_NAME_TO_ORIGINAL_NAME[organism] + "\t Taxonomy Not Retrieved ===" + "\n")
	
	
def saveGDTBTaxonomy(name, gtdbTaxonomy, outputFile, inferredFromGenus=False):
	if not inferredFromGenus:
		for organismCount in range(ORGANISM_NAME_TO_AMMOUNT[name]):
			outputFile.write(gtdbTaxonomy.replace(";", "\t") + "\t" + ORGANISM_NAME_TO_ORIGINAL_NAME[name] + "\n")
	else:
		for organismCount in range(ORGANISM_NAME_TO_AMMOUNT[name]):
			outputFile.write(gtdbTaxonomy.replace(";", "\t") + "\t" + ORGANISM_NAME_TO_ORIGINAL_NAME[name] + " Inferred_Based_on_Genus\n")
	# delet the organism from the dictionary, indicating
	# that the taxonomy was retrieved successfully
	del ORGANISM_NAME_TO_AMMOUNT[name]
		
						
def main(argv):
	initialize(argv)
	if TAXONOMY_SOURCE == "NCBI":
		getNcbiTaxonomy()
	elif TAXONOMY_SOURCE == "GTDB":
		getGTDBTaxonomy()
				
			
if __name__ == "__main__":
	main(sys.argv)

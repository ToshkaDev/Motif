#!/usr/bin/python
import sys, fileinput
from Bio import SeqIO
import collections
import traceback


if sys.argv[1] == "help" or sys.argv[1] == "-h":
	print "Usage: " + sys.argv[0] + "full|domain|names hmmsearch-results fasta-file > out-file"
	print '''Script extracts fragments of sequences from the second(2) input file (simply fasta file; contains sequences with GIids and refseqIds, or just protein names)
	specified by coordinates in the first(1) input file (results of hmmsearch).
	Options:
		full - will extract full-length protein sequences
		domain - will extract protein regions corresponding to domains
		names - will output just protein names
	'''
	sys.exit(0)
 

#PROT_NAME_DELIM = " "
#REFSEQ_POSITION_HHMMSEARCH = 1
#REFSEQ_POSITION_FASTA = 0

EVAL_THRESHOLD = 0.01
HMMSCAN_PROBABILITY = 25
MIN_LENGTH_OF_PRO_FRAGMENT = 10

FULL_PROT_OR_DOMAIN = sys.argv[1]
HMMSEARCH_HITS = sys.argv[2]
SEQUENCES = sys.argv[3]

hitFound = False
domainListBegan = False
protRefToProtInfo = collections.defaultdict(list)
shifToTheLft = 0    ###<Attention!!!
shifToTheRight = 0  ###<Attention!!!


def printFullProtein(record):
	print ">" + record.description
	print record.seq
	
def printRegionAroundTheFoundDomain(record, protRefId):
	protSeq = record.seq
	domainCount = 0
	for protInfo in protRefToProtInfo[protRefId]:
		aliStart = protInfo[0] 
		aliEnd = protInfo[1]
		if (aliStart - shifToTheLft >= 0) and (aliEnd + shifToTheRight < len(protSeq)):
			protSeq4HHDomain = protSeq[aliStart-shifToTheLft: aliEnd+shifToTheRight+1]
		elif aliStart - shifToTheLft >= 0:
			protSeq4HHDomain = protSeq[aliStart-shifToTheLft: len(protSeq)]
		elif aliEnd + shifToTheRight < len(protSeq):
			protSeq4HHDomain = protSeq[0: aliEnd+shifToTheRight+1]
		else:
			protSeq4HHDomain = protSeq[0: len(protSeq)]
		domainCount+=1

		if len(protSeq4HHDomain) >= MIN_LENGTH_OF_PRO_FRAGMENT:
			#print ">" + str(domainCount) + record.description
			print ">" + record.description
			print protSeq4HHDomain


try:	
	for record in fileinput.input(HMMSEARCH_HITS):
		record = record.strip()
		if record[:2] == ">>":
			hitFound = True
			#protRef = record.split(">> ")[1].replace(" ", "", 1)
			protRef = record.split(">> ")[1].replace("  ", " ", 1).strip()
		elif hitFound and record[:3] == "---":
			domainListBegan = True
		elif len(record) > 0 and "#" not in record and record[0] != "[":
			if hitFound and domainListBegan and record != "[No individual domains that satisfy reporting thresholds (although complete target did)]" and record != 'Alignments for each domain:' and record != "Internal pipeline statistics summary:":
				recordListWithoutSpaces = [elem for elem in record.split(" ") if len(elem) > 0]
				if float(recordListWithoutSpaces[5]) < EVAL_THRESHOLD and float(recordListWithoutSpaces[2]) >= HMMSCAN_PROBABILITY:
					aliFrom = int(recordListWithoutSpaces[9])
					aliTo = int(recordListWithoutSpaces[10])
					protRefToProtInfo[protRef].append([aliFrom, aliTo])
			if record == "Alignments for each domain:" or record == "Internal pipeline statistics summary:":
				hitFound = False
				domainListBegan = False
			
	if FULL_PROT_OR_DOMAIN == "names":
		for protein in protRefToProtInfo:
			print (protein)
	else:
		for record in SeqIO.parse(open(SEQUENCES, "r"), "fasta"):
			#protRefId = record.description.split(PROT_NAME_DELIM)[REFSEQ_POSITION_FASTA]
			protRefId = record.description.strip()
			if protRefId in protRefToProtInfo:
				if FULL_PROT_OR_DOMAIN == "full":
					printFullProtein(record)
				elif FULL_PROT_OR_DOMAIN == "domain":
					printRegionAroundTheFoundDomain(record, protRefId)			
except Exception, e:
	print "Problem happened: ", e
	print "record", record
	traceback.print_exc() 
finally:
	fileinput.close()












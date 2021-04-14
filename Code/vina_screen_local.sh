#! /bin/bash

RECEPTOR_FOLDER="/home/vadim/Documents/Projects/dCache1/AutodckVina/Receptors/Rabbit"
LIGANDS_FOLDER="/home/vadim/Documents/Projects/dCache1/AutodckVina/Ligands_pdbqt"

for receptorFile in $RECEPTOR_FOLDER/*.pdbqt; do
	receptor=`basename $receptorFile .pdbqt`
	echo Processing receptor $receptor
	mkdir -p $RECEPTOR_FOLDER/$receptor
	for ligandFile in $LIGANDS_FOLDER/*.pdbqt; do
		ligand=`basename $ligandFile .pdbqt`
		echo Processing ligand $ligand
		vina --config conf.txt --receptor $receptorFile --ligand $ligandFile --out ${RECEPTOR_FOLDER}/${receptor}/${ligand}_out.pdbqt --log ${RECEPTOR_FOLDER}/${receptor}/${ligand}_log.txt
	done
done

#!/usr/bin/env python3

import sys
from mapping_file_parse import *
from partial_capture import *
from full_capture import *
from checks import readsCount

# input path
input_path=sys.argv[1]

# Leo los archivos sam
sam_files=(glob.glob(input_path+"*.fastq"))
sam_files_dic={}

for x in sam_files:
	if "R1" in x:
		sam_files_dic["sam_R1_file"]=x
	else:	
		sam_files_dic["sam_R2_file"]=x
 
mapping_file=(input_path+"mapping.txt")

# Si existe un "#" en la primera linea del mapping file, lo remuevo
remove_hash(input_path+"mapping.txt")

# Modulo de Partial demux
# Creo carpeta donde van a ir los partial demultiplex files
createFolder(input_path+"PartialDemux")
partialDemux(mapping_file,sam_files,input_path+"PartialDemux/")

# Modulo Full Demux
# Creo carpeta donde van a ir los full demultiplex files
createFolder(input_path+"FullDemux")
sam_R1_dic=samDict(sam_files_dic["sam_R1_file"])
sam_R2_dic=samDict(sam_files_dic["sam_R2_file"])
fullDemux(input_path+"PartialDemux/",sam_R1_dic,sam_R2_dic,input_path+"FullDemux/")

# Chequeo de sequencias
readsCount(input_path)


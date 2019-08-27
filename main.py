#!/usr/bin/env python3

import sys
from partial_capture import *
from full_capture import *
from checks import readsCount
from file_manage import removeFolder

# input path
input_path=sys.argv[1]

# Leo los archivos sam
sam_files=(glob.glob(input_path+"*.fastq"))

mapping_file=(input_path+"mapping.txt")

# Modulo de Partial demux
# Creo carpeta donde van a ir los partial demultiplex files
createFolder(input_path+"PartialDemux")
partialDemux(mapping_file,sam_files,input_path+"PartialDemux/")

# Modulo Full Demux
# Creo carpeta donde van a ir los full demultiplex files
createFolder(input_path+"FullDemux")
sam_R1_dic=samDict(sam_files)
sam_R2_dic=samDict(sam_files)
fullDemux(input_path+"PartialDemux/",sam_R1_dic,sam_R2_dic,input_path+"FullDemux/")

# Chequeo de sequencias
readsCount(input_path)

# Elimino carpeta temporal de partial capture
removeFolder(input_path+"PartialDemux/")
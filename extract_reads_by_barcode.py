#!/usr/bin/env python3

import glob
import pandas as pd
from file_manage import createFolder


# input files
# SAM_R1.fastq, SAM_R1.fastq, mapping_barcodes

# output files
# R1_halfCapture.fastq, R2_halfCapture.fastq


# input path
input_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/"

# Creo carpeta donde van a ir los partial demultiplex files
createFolder(input_path+"PartialDemux")

# output path
output_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/PartialDemux/"

# Si existe un "#" en la primera linea del mapping file, lo remuevo
with open(input_path+"mapping.txt") as barcodes_file:
	lines=barcodes_file.readlines()
	if lines[0][0]=="#":
		lines[0]=lines[0][1:]
with open(input_path+"mapping.txt","w") as barcodes_file:
	barcodes_file.writelines(lines)

# Creo un diccionario donde el Key es la locacion y el value el barcode
dataset=pd.read_csv(input_path+"mapping.txt",delimiter="\t") 
barcodes_dic=dict(zip(dataset.SampleID,dataset.BarcodeSequence))   

# Leo los archivos fastq 
fastq_files=(glob.glob(input_path+"/*.fastq"))

for fastq in fastq_files:
	print(fastq)
	
	fastq_name=fastq.split("/")[-1]
	if "R1" in fastq_name:
		fastq_name ="R1"
	else:
		fastq_name="R2"
	
	f=open(fastq,"r")
	lines=f.readlines()
	cantidad_lineas=(len(lines))
	f.close()
	for location in barcodes_dic:
		out_file=open(output_path+location+"_"+fastq_name+"_"+"partialCapture"+"."+"fastq","w")
		line_index=1
		while line_index < cantidad_lineas:
			sequence_check=lines[line_index][0:8]
			if sequence_check==barcodes_dic[location]:
				out_file.write(lines[line_index-1])
				out_file.write(lines[line_index])
				out_file.write(str(line_index-1)+"\n")				
			line_index=line_index+4
		out_file.close()
	

#!/usr/bin/env python3

import glob

# input 
# Directory with fastq files

# input path
input_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/FullDemux/"
# output path
output_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/FullDemux/"

fastq_files=(glob.glob(input_path+"/*.fastq"))
fastq_files.sort()


def readsNumber(fastq_file):
	f=open(fastq_file,"r")
	lines=f.readlines()
	numberOfLines=len(lines)//4
	return str(numberOfLines)
	
# Creo un archivo con un resumen de lecturas reads de cada muestra
salida=open(output_path+"reads_counts.txt","w")
for fastq in fastq_files:	
	fastq_name=fastq.split("/")[-1][:-6]
	salida.write(fastq_name+"\t"+readsNumber(fastq)+"\n")
		
salida.close()

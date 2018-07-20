#!/usr/bin/env python3

import glob

def readsNumber(fastq_file):
	f=open(fastq_file,"r")
	lines=f.readlines()
	numberOfLines=len(lines)//4
	return str(numberOfLines)

def readsCount(input_path,out_path):
	
	print("---Read Counts Check---")
	
	fastq_files=(glob.glob(input_path+"/*.fastq"))
	fastq_files.sort()	
	salida=open(out_path+"reads_counts.txt","w")
	
	for fastq in fastq_files:	
		fastq_name=fastq.split("/")[-1][:-6]
		salida.write(fastq_name+"\t"+readsNumber(fastq)+"\n")
			
	salida.close()
	
	return 0
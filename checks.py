#!/usr/bin/env python3

import glob

def readsNumber(fastq_file):
	f=open(fastq_file,"r")
	lines=f.readlines()
	numberOfLines=len(lines)//4
	return str(numberOfLines)

def readsCount(input_path):
	
	print("---Check---")
	salida=open(input_path+"reads_counts.txt","w")
	
	fastq_files=(glob.glob(input_path+"/FullDemux/"+"*.fastq"))
	fastq_files.sort()	
	
	fastq_demux_sum=0
	
	for fastq in fastq_files:
			
		fastq_name=fastq.split("/")[-1][:-6]
		reads_count=readsNumber(fastq)
		salida.write(fastq_name+"\t"+reads_count+"\n")
		fastq_demux_sum = fastq_demux_sum + int(reads_count)
		
	salida.write("suma"+"\t"+str(fastq_demux_sum)+"\n")
	
	sam_files=(glob.glob(input_path+"SAM*"))
	
	sam_sum=0
	
	for sam in sam_files:
			
		sam_name=fastq.split("/")[-1][:-6]
		reads_count=readsNumber(sam)
		salida.write(sam_name+"\t"+reads_count+"\n")
		sam_sum = sam_sum + int(reads_count)
		
	salida.write("suma"+"\t"+str(sam_sum)+"\n")
	
	salida.write("Porcentaje de perdida de reads:"+"\t"+str(100-(fastq_demux_sum*100/sam_sum))+"\n")
			
	salida.close()
	
	return 0

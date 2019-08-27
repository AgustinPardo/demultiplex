#!/usr/bin/env python3

#import pandas as pd
from file_manage import createFolder

def partialDemux(mapping,sam_files,out_path):
	
	dataset=open(mapping,"r")
	lines=dataset.readlines()
	dataset.close()
	barcodes_dic={}
	
	for line in lines:
		if line[0:8] != "SampleID":
			line=line.rstrip("\n")
			line_splited=line.split("\t")
			barcodes_dic[line_splited[0]+"_"+line_splited[2]]=[line_splited[1],line_splited[2],line_splited[3]]
	
	fastq_files=sam_files
	
	for fastq in fastq_files:	
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
			out_file=open(out_path+location+barcodes_dic[location][2]+"_"+fastq_name+"_"+"partialCapture"+"."+"fastq","w")
			line_index=1
			while line_index < cantidad_lineas:
				sequence_check=lines[line_index][0:8]
				if sequence_check==barcodes_dic[location][0]:
					out_file.write(lines[line_index-1])
					out_file.write(lines[line_index])
					out_file.write(str(line_index-1)+"\n")				
				line_index=line_index+4
			out_file.close()
			
	return 0

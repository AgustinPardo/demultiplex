#!/usr/bin/env python3

import os
import glob
from file_manage import *

def samDict(sam_file):
	sam_file=open(sam_file,"r")
	sam_lines=sam_file.readlines()
	sam_lines_number=len(sam_lines)
	line_index=0
	sam_dic={}
	while line_index < sam_lines_number:
		sam_dic[line_index]=[sam_lines[line_index],
							sam_lines[line_index+1],
							sam_lines[line_index+2],
							sam_lines[line_index+3]
							]
		line_index=4+line_index
	sam_file.close()
	return sam_dic

def fullDemux(partialDemux_path,sam_R1_dic,sam_R2_dic,out_path):
	
	# Remuevo los archivos del directorio de salida con formato fastq
	removeTypeFile("fastq",out_path)	

	# Leo los archivos fastq de PartialDemux
	fastq_partialDemux_files=(glob.glob(partialDemux_path+"/*.fastq"))

	# Creo los full capture files
	for fastq in fastq_partialDemux_files:
	
		fastq_file=open(fastq,"r")
		fastq_lines=fastq_file.readlines()
		fastq_number_of_lines=len(fastq_lines)

		
		fastq_name=fastq.split("/")[-1]
		fastq_name=fastq_name[:-24]			
		
		fullcapture_R1_file=open(out_path+fastq_name+"_R1"+".fastq","a")
		fullcapture_R2_file=open(out_path+fastq_name+"_R2"+".fastq","a")
		
		line_index=2	
		while line_index < fastq_number_of_lines:
			
			read_index=fastq_lines[line_index].rstrip("\n")
			capture_R1=sam_R1_dic[int(read_index)]
						
			fullcapture_R1_file.write(capture_R1[0])
			fullcapture_R1_file.write(capture_R1[1])
			fullcapture_R1_file.write(capture_R1[2])
			fullcapture_R1_file.write(capture_R1[3])
			
			capture_R2=sam_R2_dic[int(read_index)]
			
			fullcapture_R2_file.write(capture_R2[0])
			fullcapture_R2_file.write(capture_R2[1])
			fullcapture_R2_file.write(capture_R2[2])
			fullcapture_R2_file.write(capture_R2[3])
		
			line_index=line_index+3		
		
			
		fullcapture_R1_file.close()
		fullcapture_R2_file.close()

	return 0

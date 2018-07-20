#!/usr/bin/env python3

import os
import glob
from file_manage import *


# input files
	# SAM_R1.fastq, SAM_R1.fastq
	# R1_halfCapture.fastq, R2_halfCapture.fastq

# output files
	# R1_FullCapture.fastq, R2_FullCapture.fastq

# input sam path
input_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/"
# input partial demux path
input_partialDemuxpath="/home/agustin/laura_Raiger_amplicones/Otoño 2016/PartialDemux/"

# Creo carpeta donde van a ir los full demultiplex files
createFolder(input_path+"FullDemux")
# output path
output_FullDemux_path="/home/agustin/laura_Raiger_amplicones/Otoño 2016/FullDemux/"
        
# Leo los archivos fastq de PartialDemux
fastq_partialDemux_files=(glob.glob(input_partialDemuxpath+"/*.fastq"))

# Creo diccionarios con los sam donde la key es la posicion y los valores el id de la read, la secuencia, +, y la calidad

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

sam_R1_dic=samDict("/home/agustin/laura_Raiger_amplicones/Otoño 2016/SAM1-16_S4_L001_R1_001.fastq")
sam_R2_dic=samDict("/home/agustin/laura_Raiger_amplicones/Otoño 2016/SAM1-16_S4_L001_R2_001.fastq")
	
# Remuevo los archivos del directorio de salida con formato fastq
removeTypeFile("fastq",output_FullDemux_path)

# Creo los full capture files
for fastq in fastq_partialDemux_files:
	print(fastq)
	
	fastq_file=open(fastq,"r")
	fastq_lines=fastq_file.readlines()
	fastq_number_of_lines=len(fastq_lines)

	
	fastq_name=fastq.split("/")[-1]
	fastq_name=fastq_name[:-24]
		
	
	fullcapture_R1_file=open(output_FullDemux_path+fastq_name+"_R1_"+"FullCapture"+".fastq","a")
	fullcapture_R2_file=open(output_FullDemux_path+fastq_name+"_R2_"+"FullCapture"+".fastq","a")
	
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


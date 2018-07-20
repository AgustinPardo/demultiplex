#!/usr/bin/env python3

def remove_hash(mapping_file):
	with open(mapping_file) as barcodes_file:
		lines=barcodes_file.readlines()
		if lines[0][0]=="#":
			lines[0]=lines[0][1:]
	with open(mapping_file,"w") as barcodes_file:
		barcodes_file.writelines(lines)
	return 0

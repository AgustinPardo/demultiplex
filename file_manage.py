#!/usr/bin/env python3

import os
import glob
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory ' +  directory)
    return 0

def removeTypeFile(TypeFile,directory):
	for zippath in glob.iglob(os.path.join(directory, "*."+TypeFile)):
		os.remove(zippath)
	return 0

def removeFolder(directory):
	# Delete all contents of a directory using shutil.rmtree() and  handle exceptions
	try:
	   shutil.rmtree(directory)
	except:
	   print('Error while deleting directory')
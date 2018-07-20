#!/usr/bin/env python3

import os
import glob

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

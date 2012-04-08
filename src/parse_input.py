#!/usr/bin/env python 

import pickle
import sys
import re 

#This script allows reading of the input of the data given to us by cs181 assignment 2. 

if len(sys.argv) < 2:
	raise Exception("Usage: input.py <input> <output>")

c_filename, c_outputname	= 		sys.argv[1:]

def oneParse():
	f = open(c_filename,"r")
	g = f.readlines()
	dummy = []
	outputlist = [] 
	for line in g:
		if line.startswith("#"):
			if dummy:
				outputlist.append(dummy) 
			dummy = [] 
		else:
			dummy.append(line) 
	return outputlist 

def twoParse():
	dummy = [] 
	outputlist = []
	rawlist = oneParse()
	for matrix in rawlist:
		if dummy:
			outputlist.append(dummy)
		dummy = []  
		for element in matrix:
			row = map(float,re.findall(r"\d+",element))
			dummy.append(row) 
	return outputlist 

pickle.dump(twoParse(), open(c_outputname,"w"))
 

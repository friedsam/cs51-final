#!/usr/bin/env python 

from numpy import * 
import pickle
import sys
import re 

#This script allows reading of the input of the data given to us by cs181 assignment 2. This takes in an arbitrary number of txt files as input. 

if len(sys.argv) < 1:
	raise Exception("Usage: parse_input.py <input.txt>")

c_listFilename 		= sys.argv[1:]
c_listOutputname 	= map(lambda x: "tmp/" + x.replace(".txt",".pkl"), c_listFilename)
c_listZip		= zip(c_listFilename,c_listOutputname)

#Sequential Code:
#Could be done in one step, but more modular this way. 

def pFormat( filename ):
	f = open( filename,"r" )
	g = f.readlines()
	dummy = []
	outputlist = [] 
	for line in g:
		if line.startswith("#"):
		#then initialize
			if dummy:
				outputlist.append([dummy,label])
			label = re.findall(r"\d+",line)[0] 
			dummy = [] 
		else:
			dummy.append(line)
	#Hack to get the last element
	if outputlist[len(outputlist)-1][0] != dummy:
		outputlist.append([dummy,label]) 
	return outputlist 

def pExtract( filename ):
	outputlist = []
	rawlist = pFormat( filename )
	for matrix,label in rawlist:
		#assuming these are castable as int, 
		#which is a reasonable assumption 
		label = int(re.findall(r"\d+",label)[0])
		dummy = []  
		for element in matrix:
			row = map(float,re.findall(r"\d+",element))
			dummy.append(row)
		outputlist.append([dummy,label])
	return outputlist 

#Execute 
if __name__ == "__main__":
	for inputf, outputf in c_listZip:
		pickle.dump( pExtract( inputf ), open( outputf,"w" ) ) 
		print("Parsing %s complete!" % outputf)

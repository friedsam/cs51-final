#!/usr/bin/env python 

from numpy import * 
import pickle
import sys
import re 
import os 

#This script allows reading of the input of the data in the NMIST database.This takes in an arbitrary number of txt files as input. 
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
		outputlist.append([array(dummy),label])
	return outputlist 

def toColMat( filename ):
        '''gets pairlist and turns into a 
	tuple containing: a (196) x n matrix, and 
	a list of length n containing the labels for 
	each data point, where n is the number 
	of data points.'''
	pairlist = pExtract( filename )
        outputarray = empty((1,196))
        dummydata = None
        dummylabel = []
        for aData,label in pairlist:
                dummydata = [aData.flatten()]
                outputarray = vstack([outputarray, dummydata])
                dummylabel.append(label)
        outputarray = outputarray[1:]
        outputarray = outputarray.T
        return (outputarray,dummylabel)


#Run Time  
if __name__ == "__main__":
	if len(sys.argv) < 1:
        	raise Exception("Usage: parse_input.py <input.txt>")
	c_listFilename          = map(lambda x: os.path.abspath(x), sys.argv[1:])
	c_listOutputname        = map(lambda x: x.replace(".txt","_colmat.pkl"), c_listFilename)
	c_listZip               = zip(c_listFilename,c_listOutputname)
	print c_listZip
	print("Initializing ... \n")
	for inputf, outputf in c_listZip:
		print("Parsing %s ...\n" % inputf)
		pickle.dump( toColMat( inputf ), open( outputf, "w" ) ) 
		print("Parsing %s complete!\n" % outputf)
	print("Process Complete. \n") 

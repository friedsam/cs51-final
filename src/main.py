#!/usr/bin/env python
from numpy import * 
import pickle
import sys
import csv 
#import parse_input
#import parse_ouput 
#import etc ... 


#This is the main execution python script. 
#In particular, this will contain all top-level functions 
#necessary to manipulate the data 

#Load all files necessary into appropriate pickle format

#Top Level Functions
#Maybe if these are really slow, I should bounce them down to 

#individual files and respective pkl components 

#need to sort, keep track of k-means centroids, treat each of them differently. 

#Data really needs to be renormalized, so that it takes values between 0 and 255, 
#and not arbitrary values. Should we use standard linear normalization?
#but I think this misses the point, because we are not using minimum error formulation, 
#but rather maximum variance formulation.  

c_fileTest1k	=	"../data/handwriting/tmp/test-1k.pkl"
c_fileVal1k	=	"../data/handwriting/tmp/validation-1k.pkl"
c_fileTrain9k	=	"../data/handwriting/tmp/training-9k.pkl"

c_fileTest1k_colmat 	= "../data/handwriting/tmp/test-1k_colmat.pkl"
c_fileVal1k_colmat	= "../data/handwriting/tmp/validation-1k_colmat.pkl"
c_fileTrain9k_colmat	= "../data/handwriting/tmp/training-9k_colmat.pkl" 

c_listTest1k 	=	pickle.load(open(c_fileTest1k,"r"))
c_listVal1k	=	pickle.load(open(c_fileVal1k,"r"))
c_listTrain9k	=	pickle.load(open(c_fileTrain9k,"r"))

 
def initialize( pairlist ):
	outputlist = [] 
	for data,label in pairlist:
		outputlist.append( [array(data), label] ) 
	return outputlist 

c_listParsePKL 	=	[ initialize( c_listTest1k ), initialize( c_listVal1k ), initialize( c_listTrain9k ) ] 
c_listParseFile	=	[ c_fileTest1k_colmat, c_fileVal1k_colmat, c_fileTrain9k_colmat ] 
c_listParseZip	=	zip(c_listParsePKL, c_listParseFile)

def unzip( pairlist ):
	l1 = []
	l2 = [] 
	for data,label in pairlist:
		l1.append(data) 
		l2.append(label)
	return (l1,l2) 
		
def getn( pairlist, digit ):
	'''crawls through list and finds only those with the 
	specified label'''
	outputlist = [] 
	d = digit 
	for data, label in pairlist:
		if label == d:
			outputlist.append([data,label])
		else:
			continue 
	return outputlist 

#need to fix abnormal nesting behavior

def labelsort( pairlist ):
	'''is a function that returns the [data,label] and sorts 
	from lowest to highest based on the labels (0-9).
	Returns a [data',label'] list. '''
	outputlist = []
	for i in range(0,10):
		outputlist.append(getn( pairlist, i ) )
	return outputlist

#def fromDataVec( vec ):
#	'''turns (d x d) dimensional vector into 
#	its matrix counterpart. '''
#	outputlist = []
		
	

def toDataMat( pairlist ):
	'''gets pairlist and turns into (196) x n matrix, where 
	n is the number of data points.'''
	outputarray = empty((1,196)) 
	dummy = None   
	for aData,label in pairlist:
		dummy = [aData.flatten()] 
		outputarray = vstack([outputarray, dummy])
	outputarray = outputarray[1:]
	outputarray = outputarray.T	
	return outputarray 

#This still needs to be fixed. 

def fromDataMat( mat ):
	'''gets matrix of data points and converts into 
	matrix of image matrices'''
	outputlist = []
	matT = mat.T
	for row in matT:
		outputlist.append(fromDataVec( row )) 
	return outputlist 

#remember the method a.tolist() to make arrays into lists. 
#will come in handy when you want to de-array things. 

#pypng can save numpy arrays as images.  
#also try looking at montage sheet 
		
#Test Execute

if __name__ == "__main__":
	print("Creating column matrix files ... \n")
	for pairlist, filename in c_listParseZip: 
		with open( filename, "w" ) as outputf:
			print("parsing %s\n" % filename )
			pickle.dump(toDataMat( pairlist ), outputf )
	print("Done!\n")

#toDataMat( initialize( c_listTest1k ) )

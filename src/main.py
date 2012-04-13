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

#BLAHBLAHBLAH

#Top Level Functions
#Maybe if these are really slow, I should bounce them down to 

#individual files and respective pkl components 

c_fileTest1k	=	"../data/handwriting/test-1k.pkl"
c_fileVal1k	=	"../data/handwriting/validation-1k.pkl"
c_fileTrain9k	=	"../data/handwriting/training-9k.pkl"

c_listTest1k 	=	pickle.load(open(c_fileTest1k,"r"))
c_listVal1k	=	pickle.load(open(c_fileVal1k,"r"))
c_listTrain9k	=	pickle.load(open(c_fileTrain9k,"r"))
 
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

def labelsort( pairlist ):
	'''is a function that returns the [data,label] and sorts 
	from lowest to highest based on the labels (0-9).
	Returns a [data',label'] list. '''
	outputlist = []
	for i in range(0,10):
		outputlist.append(getn( pairlist, i ) )
	return outputlist

#Test Execute

if __name__ == "__main__":
	with open("sort_test.pkl","w") as outputf:
		pickle.dump(labelsort( c_listTrain9k ), outputf)
		print("Done!")	

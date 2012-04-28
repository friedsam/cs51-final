#!/usr/bin/env python

from numpy import * 
import pickle
import sys
import csv 
import kmeans 
import pca 

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

#c_fileTest1k_colmat 	= "../data/handwriting/tmp/test-1k_colmat.pkl"
#c_fileVal1k_colmat	= "../data/handwriting/tmp/validation-1k_colmat.pkl"
#c_fileTrain9k_colmat	= "../data/handwriting/tmp/training-9k_colmat.pkl" 

#c_listTest1k 	=	pickle.load(open(c_fileTest1k_colmat,"r"))
#c_listVal1k	=	pickle.load(open(c_fileVal1k_colmat,"r"))
#c_listTrain9k	=	pickle.load(open(c_fileTrain9k_colmat,"r"))

#=================== HELPER FUNCTIONS ========================#
	
def eucDist(v1,v2):
        '''Euclidean Distance'''
        return linalg.norm(v1-v2)

def getn( inputpair, digit ):
	'''crawls through list of labels and finds 
	data with the specified label'''
	dummyindex = []
	outputarray = empty((1,196)) 
	d = digit 
	dataMat, labelLst = inputpair
	numRow, numCol = dataMat.shape  
	for i in range(0,len(labelLst)):
		if labelLst[i] == d:
			dummyindex.append(i) 
	for j in dummyindex:
		outputarray = vstack( [outputarray, [dataMat[:,j]]] )
	outputarray = outputarray[1:]
	return outputarray.T,d
	
def labelsort( inputpair ):
	'''is a function that returns the [data,label] and sorts 
	from lowest to highest based on the labels (0-9).
	Returns a [data',label'] list. '''
	outputlist = []
	for i in range(0,10):
		outputlist.append(getn( inputpair, i ))
	return outputlist

#THESE ARE PROBABLY COMPLETELY UNNECESSARY 

#def fromDataVec( vec ):
#       '''turns (d x d) dimensional vector into 
#       its matrix counterpart. '''
#       outputlist = []

#def fromDataMat( mat ):
#       '''gets matrix of data points and converts into 
#       matrix of image matrices'''
#       outputlist = []
#       matT = mat.T
#       for row in matT:
#               outputlist.append(fromDataVec( row )) 
#       return outputlist 

#remember the method a.tolist() to make arrays into lists. 
#will come in handy when you want to de-array things. 


#=================== FEATURE EXTRACTION ======================#

def centroidPCA( inputpair, k ):
	'''get the centroid list for later implementation in
	conjunction with PCA. The input is the sorted list given 
	by the output of the function labelsort.'''
	sortlist = labelsort( inputpair )
	dummylist = []
	for item in sortlist:
		dataMat, digit = item 
		clusters, centroids = kmeans.makeClusters(dataMat, k)
		for clutster_i in clusters:
			dummylist.append((cluster_i, digit))
	return dummylist 

#=================== DATA PROJECTION =========================#

def getProjData( training, test, k, D ):
	'''Obtains linear projection transformation T
	taking R^196 onto R^D, projects the 
	corresponding centroids of the k clusters,
	projects the test data onto R^D.
	Outputs the test dataMat of D x n dimensions
	and gives the k x 10 centroids, each of them
	in R^D. '''
	dummycentroid = [] 
	trainingProj, T =  pca.PCA( training, D ) 
	for cluster_i, digit in centroidPCA( trainingProj, k ):
		dummycentroid.append(dot(T, cluster_i), digit)
	testProj = dot( T,test )
	return testProj, dummycentroid 

#==================== STATSTICAL INFERENCE ======================#
					
def makeDist(vec, centroidLst):
        '''Makes list of containing the 
        Euclidean Distance between vec and every 
        element in the centroidLst.'''
        dummy = []
        for cen,lab in centroiLst:
                dummy.append(eucDist(vec,cen))
        return dummy

def assign(testMat, centroidLst):
        '''returns list of labels
        assigned to each column vector in 
        the test matrix'''
        dummy = []
        numRow, numCol = testMat.shape
        for i in range(0,numCol):
                minVal = min(makeDist(testMat[:,i],centroidLst))
                cen,lab = centroidLst.index(minVal)
                dummy.append(lab)
        return dummy

def makeTriple( trainPair, testPair, centroidLst ):
        '''Makes a triple containing the datapoint, 
        true label, and assigned label.'''
	trainMat, trainLabel = trainPair 
        testMat, labelLst = testPair  
        assignLablst = assign(testMat, centroidLst)
        trueLablst = labelLst

	#I don't think this zip functions works properly
	#because I think I need to take the transpose of
	#the function.. check this later.  
        return zip(trainMat.T, trueLablst, assignLablst )


#==================== RUN TIME BEHAVIOR =======================#

#if __name__ == "__main__": 
#	c_trainf, c_testf, c_triple = sys.argv[1:4]
#	k = int(sys.argv[4])
#	D = int(sys.argv[5]) 
#	train 	= pickle.load(open(c_trainf)) 
#	test 	= pickle.load(open(c_testf))   
#	#Run 
#	testProj, centroidLst = getProjData( train, test, k, D )
#	#Save this 
#	pickle.dump(makeTriple( train, testProj, centroidLst ),\
#		open(c_triple, "w")) 
#	#And feed into montage later. 

#I need to debug part by part. 
	

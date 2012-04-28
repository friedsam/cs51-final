#!/usr/bin/env python

from numpy import *
import pickle
import pca 
import kmeans 
import sys  

c_num_comps 	=	50 
inputMat 	= 	something 

origMat, origLab = inputMat

projmat, vecs = pca.PCA(mat, comps)
clusters, centroids = kmeans.makeClusters(data, number_of_clusters)  

def eucDist(v1,v2):
	return linalg.norm(v1-v2) 

def makeDist(vec, centroidLst) 
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

def makeTriple( testPair, centroidLst ):
	testMat, labelLst = testPair
	assignLablst = assign(testMat, centroidLst) 
	trueLablst = labelLst
	return zip(origMat, trueLablst, assignLablst ) 

	


 
	
		

		

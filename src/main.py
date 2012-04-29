#!/usr/bin/env python

from numpy import * 
import pickle
import sys
import csv 
import kmeans 
import pca 
import montage 
import os 

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
	d = digit 
	dataMat, labelLst = inputpair
	numRow, numCol = dataMat.shape 
	outputarray = empty((1,numRow)) 
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
		for vec in centroids:
			#initialize list to numpy arrays 
			vec = array(vec) 
			dummylist.append((vec, digit))
	return dummylist 

#=================== DATA PROJECTION =========================#

#Currently k-means is not behaving so well with respect to 
#column operations. Need to transpose input matrix, and 
#tranpose it back to get the column representation.  

def getProjData( training, test, k, D ):
	'''Obtains linear projection transformation T
	taking R^196 onto R^D, projects the 
	corresponding centroids of the k clusters,
	projects the test data onto R^D.
	Outputs the test dataMat of D x n dimensions
	and gives the k x 10 centroids, each of them
	in R^D. '''
	print "Running getProjData ... \n"
	testMat, testlab = test  
	trainingProj, T =  pca.PCA( training, D ) 
	centroidLst = centroidPCA( trainingProj, k )
	testProj = dot( T,testMat )
	return testProj, centroidLst

#==================== STATSTICAL INFERENCE ======================#
					
def makeDist(vec, centroidLst):
        '''Makes list of containing the 
        Euclidean Distance between vec and every 
        element in the centroidLst.'''
        dummy = []
        for cen,lab in centroidLst:
                dummy.append(eucDist(vec,cen))
        return dummy

def assign(testMat, centroidLst):
        '''returns list of labels
        assigned to each column vector in 
        the test matrix'''
	#remember I have to assign the labels of the 
	#sorted label list. 
        dummy = []
        numRow, numCol = testMat.shape
        for i in range(0,numCol):
		distLst = makeDist(testMat[:,i],centroidLst)
                minVal = min(distLst)
		cen,lab = centroidLst[distLst.index(minVal)]
                dummy.append(lab)
        return dummy

def makeTriple( training, test, k, D ):
        '''Makes a triple containing the datapoint, 
        true label, and assigned label.'''
	trainMat, trainLab = training
        testMat, testLab = test
	testProj, centroidLst = getProjData( training, test, k, D ) 
        assignLablst = assign(testProj, centroidLst)
        trueLablst = testLab

	#I don't think this zip functions works properly
	#because I think I need to take the transpose of
	#the function.. check this later.  
        return zip(testMat.T, trueLablst, assignLablst )

def confusion( triple, digit ):
	'''Makes a confusion matrix for each digit, and 
	creates an output for inputting into the montage
	function. Note: confusion matrix is C_{i,j} such
	that C_{1,1} = TP, C_{1,2} = FN, C_{2,1} = FP,
	C_{2,2} = TN . '''
	d = digit
	length = len(triple)
	dummylist = [] 
	TP = FN = FP = TN = 0
	for vec,true,assigned in triple:
		if d == true == assigned:
			dummylist.append((vec,"TP"))
			TP += 1  
		elif (d != true) & (d == assigned):
			dummylist.append((vec,"FP"))
			FP +=1
		elif (d == true ) & (d != assigned):
			dummylist.append((vec,"FN"))
			FN +=1
	TN = length - (TP+FN+FP)
	confusionarray = array([[TP,FN],[FP,TN]]) 
	return dummylist, confusionarray 			
			 

#==================== RUN TIME BEHAVIOR =======================#

def run( inputDataFilepath, inputTrainingFilepath, outputFilepath, outputDirpath, numClusters, numComponents ):

    c_dest_dir  = outputDirpath + "/"
    train 	= pickle.load(open(inputTrainingFilepath))
    test 	= pickle.load(open(inputDataFilepath))

    print "making triple ... \n"
    triple = makeTriple(train, test, numClusters, numComponents)
    print "dumping pickle ... \n"
    pickle.dump(triple, open(c_dest_dir + "triple.pkl", "w"))
    for i in range(0,10):
        confPair = confusion(triple,i)
        print "dumping confusion", str(i)
        pickle.dump( confPair, open( c_dest_dir + "conf_" + str(i) + ".pkl","w" ) )
        montagelist, confusionarray = confPair
        print "\n Making montage", str(i)
        montage.colorsMontage( montagelist, c_dest_dir + str(i) + ".png")	

if __name__ == "__main__": 
	c_trainf, c_testf, c_dir = sys.argv[1:4]
	k = int(sys.argv[4])
	D = int(sys.argv[5]) 
	c_basename = os.path.basename(c_testf).split(".")[0]
	c_triple = c_basename + "_triple.pkl"
	c_confusion = c_basename + "_confusion.pkl" 
	train 	= pickle.load(open(c_trainf)) 
	test 	= pickle.load(open(c_testf))   
	
	#Save this
	print "making triple ... \n" 
	triple = makeTriple(train,test,k,D)
	print "dumping pickle ... \n"
	pickle.dump(triple,open(c_dir + c_triple, "w")) 
	for i in range(0,10):
		confPair = confusion(triple,i)
		print "dumping confusion", str(i)
		pickle.dump( confPair, open( c_dir + c_basename + \
			 "_confusion" + str(i) + ".pkl","w" ) )
		montagelist, confusionarray = confPair
		print "\n Making montage", str(i)
		montage.colorsMontage( montagelist, c_dir + c_basename +\
			"_montage" + str(i) + ".jpg")	
				

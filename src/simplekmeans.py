#!/usr/bin/env python
# encoding: utf-8

import montage
import pickle
import string
from numpy import *
from kmeans import *

# remember to transpose!

# takes a clusters object and a filename and makes .jpg's
def kmeansClustersJpgs(clusters, filename):
    for j in range(len(clusters)):
        name = string.rstrip(filename,".pkl")
        name = name + "clust" + str(j) + "of" + str(len(clusters)-1) + ".jpg"
        montage.montage(clusters[j], open(name, "w"))

# filename should be a pickle in format of datapoints
# i.e parray is 1000 x 196 array
def simplekmeans(filename, k):
    parray = pickle.load(open(filename))
    (clusters, centroids) = makeClusters(parray, k)
    kmeansClustersJpgs(clusters, filename)

# simplekmeans from test-1k.pkl format
def simplekfromscratch(filename, k):
    pkl = pickle.load(open(filename))
    leng = len(pkl)
    w = [0] * leng
    for k in range(leng):
        w[k] = array(pkl[k][0]).ravel()
    (clusters, centroids) = makeClusters(array( w), k)
    kmeansClustersJpgs(clusters, filename)

def run( inputFilepath, outputFilepath, outputDirpath, kNum):
    print "Run simplekmeans ..."
    simplekmeans(inputFilepath, kNum)

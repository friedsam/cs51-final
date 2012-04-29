#!/usr/bin/env python
# encoding: utf-8

import montage
import pickle
import string
from numpy import *
from kmeans import *

# remember to transpose!

def kmeansClustersJpgs(clusters, filename, outputDirpath):
# takes a clusters object and a filename and makes .jpg's
    for j in range(len(clusters)):
        name = outputDirpath + "/" + str(j) + ".png"
        print("Trying create image file at: %s" % name)
        montage.montage(clusters[j], open(name, "w"))

def simplekmeans(filename, outputDirpath, k):
# filename should be a pickle in format of colmat
    parray = pickle.load(open(filename))
    (clusters, centroids) = makeClusters(parray, k)
    kmeansClustersJpgs(clusters, filename, outputDirpath)

def simplekfromscratch(filename, k):
# simplekmeans from test-1k.pkl format
    pkl = pickle.load(open(filename))
    leng = len(pkl)
    w = [0] * leng
    for j in range(leng):
        w[j] = array(pkl[j][0]).ravel()
    (clusters, centroids) = makeClusters(array( w).T, k)
    kmeansClustersJpgs(clusters, filename)

def run( inputFilepath, outputFilepath, outputDirpath, kNum):
    print "Run simplekmeans ..."
    simplekmeans(inputFilepath, outputDirpath, kNum)

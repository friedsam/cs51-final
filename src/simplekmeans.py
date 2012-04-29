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
    (clusters, centroids) = makeClusters(parray[0], k)
    kmeansClustersJpgs(clusters, filename, outputDirpath)

def run( inputFilepath, outputFilepath, outputDirpath, kNum):
    print "Run simplekmeans ..."
    simplekmeans(inputFilepath, outputDirpath, kNum)

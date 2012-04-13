import random as rnd
import math as m
from numpy import *


def initializeClusters(data,number_of_clusters):
    clust = [array([[]])] * number_of_clusters
    for i in range(data.shape[0]):
        rand = rnd.randint(0,number_of_clusters-1)
        if clust[rand].shape == (1,0):
            clust[rand] = append(clust[rand],[data[i,:]],1)
        else:
            clust[rand] = append(clust[rand],[data[i,:]],0)
    return clust

def getCentroids(new_clusters):
    centroids = [0]*len(new_clusters)
    for i in range(len(new_clusters)):
        centroids[i] = list(new_clusters[i].mean(axis=0))
    return centroids

def reassignClusters(centroids,data):
    clust = [array([[]])] * len(centroids)
    for i in range(data.shape[0]):
        min_ind = 0
        min_dist = calcDist(centroids[0],data[i,:])
        for j in range(1,len(centroids)):
            dist = calcDist(centroids[j],data[i,:])
            if (dist < min_dist):
                min_ind = j
                min_dist = dist
        if clust[min_ind].shape == (1,0):
            clust[min_ind] = append(clust[min_ind],[data[i,:]],1)
        else:
            clust[min_ind] = append(clust[min_ind],[data[i,:]],0)
    return clust

def calcDist(point1,point2):
    dim = len(point1)
    sq_sum = 0
    for i in range(dim):
        sq_sum = sq_sum + (point1[i] - point2[i])**2
    dist = m.sqrt(sq_sum)
    return dist

#TODO ensity needs to be changed to return list of density for each cluster
#returns the average cluster average density:
def density(clusters):
    density = 0
    centroids = [0]*len(clusters)
    for i in range(len(clusters)):
        centroids[i] = list(clusters[i].mean(axis=0))
        for j in range(len(clusters[i])):
            density += calcDist(centroids[i], clusters[i][j]) / len(clusters[i])
    return density / len(clusters)

#calculates average dissimilarity between a point and a list of points
def dissimilarity(point, lst):
    dsm = 0
    for i in range(len(lst)):
        dsm += calcDist(point, lst[i])
    return (dsm / len(lst))

def silhouette(clusters):
    #silh = []
    total = 0
    datalength = 0
    for i in range(len(clusters)):
        datalength += len(clusters[i])
        #silh.append([0] * len(clusters[i]))
        initial = 0
        if i == 0: initial = 1
        for j in range(len(clusters[i])):
            datum = clusters[i][j]
            owndsm = dissimilarity(datum, clusters[i])
            # finds lowest average dissimilarity of another cluster
            min_dsm = dissimilarity(datum, clusters[initial])
            for k in range(len(clusters)):
                if k != i:
                    new_dsm = dissimilarity(datum, clusters[k])
                    if new_dsm < min_dsm: min_dsm = new_dsm
            #silh[i][j] = 1 - owndsm / min_dsm
            total += 1 - owndsm/ min_dsm
    return total/datalength
        

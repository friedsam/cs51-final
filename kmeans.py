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



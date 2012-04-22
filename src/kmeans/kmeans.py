import random as rnd
import math as m
from numpy import *

# clusters are going to be lists of a singular cluster.
# a cluster is an arrays of data points.

# centroids are similarly a list of the data point that is the
# center for each cluster

#the data invariant is a numpty array of datapoints

# randomly assigns each data point to a cluster, returning clusters
def initializeClusters(data,number_of_clusters):
    clust = [array([[]])] * number_of_clusters
    for i in range(data.shape[0]):
        rand = rnd.randint(0,number_of_clusters-1)
        if clust[rand].shape == (1,0):
            clust[rand] = append(clust[rand],[data[i,:]],1)
        else:
            clust[rand] = append(clust[rand],[data[i,:]],0)
    return clust

# returns the centroids of some clusters
def getCentroids(clusters):
    centroids = [0]*len(clusters)
    for i in range(len(clusters)):
        centroids[i] = list(clusters[i].mean(axis=0))
    return centroids

# reassigns each data point so that it is a member of the
# cluster with thevclosest centroid
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

# simple Euclidean distance
def calcDist(point1,point2):
    dim = len(point1)
    sq_sum = 0
    for i in range(dim):
        sq_sum = sq_sum + (point1[i] - point2[i])**2
    dist = m.sqrt(sq_sum)
    return dist

# returns the average cluster average density (for evaluation)
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

# returns the average silhouette for some clusters (for evaluation)
def silhouette(clusters):
    total = 0
    datalength = 0
    for i in range(len(clusters)):
        datalength += len(clusters[i])
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
            total += 1 - owndsm/ min_dsm
    return total/datalength


# kmeans algorithm :
# takes an int number of clusters and a numpy array of data
# returns (a length num list of clusters where each cluster is a numpy array
# of its data points) paired with ( a list of the centroids).
def makeClusters(data, number_of_clusters):
    new_clusters = initializeClusters(data,number_of_clusters)
    #calculate initial centroids 
    new_centroids = getCentroids(new_clusters)
    old_centroids = []
    # beginning of loop, while new_centroids not equal old_centroids
    '''
    iters = 100
    while (iters > 0):
        old_centroids = new_centroids
        # calculate new clusters
        new_clusters = reassignClusters(new_centroids,data)
        # recalculate new centroids
        new_centroids = getCentroids(new_clusters)
        iters -= 1'''
    while (old_centroids != new_centroids):
        old_centroids = new_centroids
        # calculate new clusters
        new_clusters = reassignClusters(new_centroids,data)
        # recalculate new centroids
        new_centroids = getCentroids(new_clusters)
    return (new_clusters, new_centroids)
'''
def evals(clusters):
    print("Average cluster density: ")
    print(density(clusters))
    print("\nSilhouette of the clusters: ")
    print(silhouette(clusters))

def printPoint(datum):

    
def outputClusters(clusters):
    for i in range(len(clusters)):
        print("Printing cluster"
        print(i)
        print("\n")
        for k in range(len(clusters[i])):
            printPoint(clusters[i][k])
            print("\n")
            '''

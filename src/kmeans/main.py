import os
from numpy import *
from readData import *
from kmeans import *
import pickle
import sys 

c_filePKL, c_numclusters = sys.argv[1:]

def main():
        #read data file into array
        data = pickle.load(open(c_filePKL))
        number_of_clusters = int(c_numclusters)
        #pick initial clusters
        new_clusters = initializeClusters(data,number_of_clusters)
        print new_clusters[0]
        print new_clusters[1]
        print new_clusters[2]
        #calculate initial centroids 
        new_centroids = getCentroids(new_clusters)
        old_centroids = []
        # beginning of loop, while new_centroids not equal old_centroids
        while (old_centroids != new_centroids):
                old_centroids = new_centroids
                # calculate new clusters
                new_clusters = reassignClusters(new_centroids,data)
                # recalculate new centroids
                new_centroids = getCentroids(new_clusters)
        print "new Cluster"
        print new_clusters[0]
        print new_clusters[1]
        print new_clusters[2]
        print new_centroids
        print old_centroids

if __name__ == "__main__":
        main()

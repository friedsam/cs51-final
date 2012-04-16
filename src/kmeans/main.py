import main
from kmeans import *
from numpy import *

# takes an int number of clusters and a numpy array of data
# returns a length num list of clusters
# each cluster is a numpy array of its data points.
def makeClusters(number_of_clusters, data):
    new_clusters = initializeClusters(data,number_of_clusters)
    #calculate initial centroids 
    new_centroids = getCentroids(new_clusters)
    old_centroids = []
    # beginning of loop, while new_centroids not equal old_centroids
    '''iters = 100
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
    return new_clusters

def evals(clusters):
    print("Average cluster density: ")
    print(density(clusters))
    print("\nSilhouette of the clusters: ")
    print(silhouette(clusters))

#top level TEST code
def thingy():
        a = main.initialize(main.c_listTest1k)
        #(l1, l2) = main.unzip(a)
        data = main.toDataMat(a)
        number_of_clusters = 10
        #pick initial clusters
        new_clusters = initializeClusters(data,number_of_clusters)
        print new_clusters[0]
        print new_clusters[1]
        print new_clusters[2]
        #calculate initial centroids 
        new_centroids = getCentroids(new_clusters)
        old_centroids = []
        # beginning of loop, while new_centroids not equal old_centroids
        iters = 10
        while (iters > 0):
                old_centroids = new_centroids
                # calculate new clusters
                new_clusters = reassignClusters(new_centroids,data)
                # recalculate new centroids
                new_centroids = getCentroids(new_clusters)
                iters -= 1
        '''while (old_centroids != new_centroids):
                old_centroids = new_centroids
                # calculate new clusters
                new_clusters = reassignClusters(new_centroids,data)
                # recalculate new centroids
                new_centroids = getCentroids(new_clusters)'''
        print "new Cluster"
        print new_clusters[0]
        print new_clusters[1]
        print "clusters2\n"
        print new_clusters[2]
        #print new_centroids
        #print old_centroids


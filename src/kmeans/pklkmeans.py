from numpy import *
from kmeans import *
import pickle

# takes a filename of a pickle of a numpy array of points
# and a int for a number of clusters.
def clusterpkl(input_filename, k_num, output_filename):
    parray = pickle.load(open(input_filename))
    (clusters, centroids) = makeClusters(parray, k_num)
    f = open( output_filename, "w")
    pickle.dump( (clusters, centroids), f)
    f.close()

def getclusterspkl(filename):
    return pickle.load(open(filename, "r"))
    
'''Important Invariants:
    clusterpkl must take a pickle that is a just an array of the data points.
    getclusterspkl returns a list of the (clusters object, centroids)
    e.g. a = getclusterspkl( pickled_cluster_filename)
        a[0] -> list of clusters
        a[0][k] -> array of points that is the kth cluster
        a[1] -> list of centroids
        a[1][k] -> kth centroid (data point format)
'''

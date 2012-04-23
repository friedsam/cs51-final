from numpy import *
from kmeans import *
import pickle
import sys

# takes a filename of a pickle of a numpy array of points
# and a int for a number of clusters.
def clusterpkl(input_filename, k_num, output_filename):
    print "Loading array...\n"
    parray = pickle.load(open(input_filename))
    print "Making clusters...\n"
    (clusters, centroids) = makeClusters(parray, k_num)
    f = open( output_filename, "w")
    pickle.dump( (clusters, centroids), f)
    f.close()
    print "Done!\n"

#function to load a cluster pkl (created above)
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

c_fileInPKL, c_fileOutPKL   = sys.argv[1:3]
c_numclusters               = int(sys.argv[3])

if len( sys.argv[1:] ) < 3:
    raise Exception("Usage: python pklkmeans.py <input.pkl> <output.pkl> <number_of_clusters>")
    
if __name__ == "__main__":
    clusterpkl(c_fileInPKL, c_numclusters, c_fileOutPKL)
    

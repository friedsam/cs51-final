from numpy import *
import sys 
import pickle

#============= PCA functions =================#

def covariance(mat):
	'''Computes covariance matrix'''
	dim,numdata = mat.shape
        m = array([mean(mat,1)]).T
        new_mat = zeros((dim,dim))
        for i in range(numdata):
                xn = array([mat[:,i]]).T
                diff = (xn - m)
                new_mat = dot(diff, diff.T) + new_mat
        cov_mat = (new_mat * (1.0/(len(mat[0]))))
	return cov_mat

def eigs( mat, comps ):
	'''finds eigenvalues and associated 
	eigenvectors. '''
	val,vec = linalg.eig(mat)
	perm = argsort(-val)
	valsort = val[perm]
	vecsort = vec.T[perm].T
	return valsort[0:comps], vecsort[:,0:comps]


def PCA(inputpair, comps):
	'''Takes matrix with the datapoint in 
	each column and runs Principal Component 
	Analysis on comps number of components.
	Then, it returns a modified column matrix 
	and the linear transformation that determines 
	the projection. '''
	mat, labels = inputpair 
	dim,numdata = mat.shape
	cov_mat = covariance(mat)
	vals,vecs = eigs(cov_mat,comps)
	projmat = dot(vecs.T,mat)
	return (projmat,labels),vecs.T 

def variance(mat,comps):
	'''evaluation/test method to make sure 
	that the principal components actually 
	correspond to largest eigenvalues'''
        dim,numdata = mat.shape
        cov_mat = covariance(mat,dim,numdata)
        vals,vecs = eigs(cov_mat,dim)
	if len(vals) < comps:
		raise Exception("Not enough real eigenvalues.")
	varmat = zeros(comps)
	for i in range(comps):
		varmat[i] = dot(dot(vecs[:,i].T,cov_mat),vecs[:,i])

	return varmat

def decreasing(mat,comps):
	'''evaluation/test method to make sure 
	the eigenvalues corresponding to the 
	principal components are in decreasing 
	order'''
	dim,numdata = mat.shape
	cov_mat = covariance(mat,dim,numdata)
	vals,vecs = eigs(cov_mat,dim)
	if len(vals) < comps:
		raise Exception("Not enough real eigenvalues.")
	for i in range(comps-1):
		if vals[i] < vals[i+1]:
			return False

	return True

#================ RUN TIME BEHAVIOR =======================#

if __name__ == "__main__":
	c_fileInPKL, c_fileOutPKL       = sys.argv[1:3]
	c_numcomps                      = int(sys.argv[3])
	if len( sys.argv[1:] ) < 3:
        	raise Exception("Usage: python pca.py <input.pkl> \
			 <output.pkl> <number_of_components>")
	pkl = pickle.load(open(c_fileInPKL))
	print "Generating pickle file(s) ..."
	with open(c_fileOutPKL,"w") as outputf:
		pickle.dump(PCA( pkl, c_numcomps ), outputf )
	print "Done!"
	 

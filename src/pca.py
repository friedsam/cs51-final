from numpy import *
import sys 
import pickle

#find covariance matrix
def covariance(mat):
	dim,numdata = mat.shape
        m = array([mean(mat,1)]).T
        new_mat = zeros((dim,dim))
        for i in range(numdata):
                xn = array([mat[:,i]]).T
                diff = (xn - m)
                new_mat = dot(diff, diff.T) + new_mat
        cov_mat = (new_mat * (1.0/(len(mat[0]))))
	return cov_mat

# finds eigenvalues and associated eigenvectors; sort in decreasing order
def eigs( mat, comps ):
	#dim = mat.shape[0]
	val,vec = linalg.eig(mat)
	#for i in reversed (range(dim)):
	#	if val[i].imag != 0:
	#		val = delete(val,i,0)
	#		vec = delete(vec.T,i,0).T

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
	dim,numdata = mat.shape
	cov_mat = covariance(mat,dim,numdata)

	vals,vecs = eigs(cov_mat,dim)
	if len(vals) < comps:
		raise Exception("Not enough real eigenvalues.")
	
	for i in range(comps-1):
		if vals[i] < vals[i+1]:
			return False

	return True

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
	 

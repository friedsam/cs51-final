from numpy import *
import matrix
import sys 
import pickle

c_filePKL, c_numcomps = sys.argv[1:]

# very simple matrices for basic testing
#a = array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
#b = array([[1.,6.,2.],[6.,3.,1.]])

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
def eigs(mat, comps):
	#dim = mat.shape[0]
	val,vec = linalg.eig(mat)
	#for i in reversed (range(dim)):
	#	if val[i].imag != 0:
	#		val = delete(val,i,0)
	#		vec = delete(vec.T,i,0).T

	perm = argsort(-val)
	valsort = val[perm]
	vecsort = vec.T[perm].T
	return valsort, vecsort



def PCA(mat, comps):
	dim,numdata = mat.shape
	cov_mat = covariance(mat)
	vals,vecs = eigs(cov_mat,comps)
        #if len(vals) < comps:
	#	raise Exception("Not enough real eigenvalues.")

	projmat = dot(vecs.T,mat)
	#return projmat[0:comps]
	return projmat 

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
	print( str(PCA(pickle.load(open(c_filePKL)), c_numcomps)) )

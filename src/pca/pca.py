from numpy import *
import matrix

#a = array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
#b = array([[1.,6.,2.],[6.,3.,1.]])

def covariance(mat,dim,numdata):
        m = array(matrix.mean(mat))
        new_mat = zeros((dim,dim))
        for i in range(numdata):
                xn = array(matrix.column(mat,i))
                variance = (xn - m)
                new_mat = dot(variance, transpose(variance)) + new_mat
        cov_mat = (new_mat * (1.0/(len(mat[0]))))

	return cov_mat

def eigs(mat,dim):
	val,vec = linalg.eig(mat)
	for i in reversed (range(dim)):
		if val[i].imag != 0:
			val = delete(val,i)
			vec = delete(vec,i)

	perm = argsort(-val)
	valsort = val[perm]
	vecsort = (vec.T[perm]).T
	return valsort, vecsort


def PCA(mat, comps):
	dim,numdata = mat.shape
	cov_mat = covariance(mat,dim,numdata)
	vals,vecs = eigs(cov_mat,dim)
        if len(vals) < comps:
		raise Exception("Not enough real eigenvalues.")
	perm = argsort(-vals)
        # valsort = vals[perm]
        #vecsort = vecs[:,perm]

	#projmat = zeros((comps,numdata))
	projmat = dot(vecs.T,mat)
	#for i in range(comps):
	#	for j in range(numdata):
	#		projmat[i][j] = dot(vecsort[i],mat[:,j])

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



from numpy import *
import matrix

a = array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
b = array([[1.,6.,2.],[6.,3.,1.]])

def PCA(mat,comps):
	dim,numdata = mat.shape
        m = array(matrix.mean(mat))
        new_mat = zeros((dim,dim))
        for i in range(numdata):
                xn = array(matrix.column(mat,i))
                variance = (xn - m)
                new_mat = (variance * transpose(variance)) + new_mat
        cov_mat = (new_mat * (1.0/(len(mat[0]))))

	e,vecs = linalg.eig(cov_mat)
	EV = zeros((dim,dim))
	for i in range(dim):
		EV[i] = vecs[:,i]
	e = e[::-1]
	EV = EV[::-1]

	projmat = zeros((dim,comps))
	for i in range(comps):
		projmat[:,i] = dot(mat,EV[i])

	return projmat
	


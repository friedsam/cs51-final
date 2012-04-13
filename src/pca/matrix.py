
import random
from time import *
import cProfile
 
def zero(m,n):
    # Create zero matrix
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix
 
def rand(m,n):
    # Create random matrix
    new_matrix = [[random.random() for row in range(n)] for col in range(m)]
    return new_matrix
 
def show(matrix):
    # Print out matrix
    for col in matrix:
        print col 
 
def mult(matrix1,matrix2):
    # Matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        # Check matrix dimensions
        print 'Dimensions do not match'
    else:
        # multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix
 
def add(matrix1, matrix2):
	# matrix addition 
	if (len(matrix1[0]) != len(matrix2[0])) | ( len(matrix1) != len(matrix2) ):
		print "Dimensions do not match"
	else:
		# add with correct dimensions	
		new_matrix = zero(len(matrix1),len(matrix1[0]))
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				new_matrix[i][j] += matrix1[i][j] + matrix2[i][j]
	return new_matrix

def negate(matrix):
	new_matrix = zero(len(matrix),len(matrix[0]))
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			new_matrix[i][j] = -1 * matrix[i][j]
	return new_matrix 

def time_mult(matrix1,matrix2):
    # Clock the time matrix multiplication takes
    start = clock()
    new_matrix = mult(matrix1,matrix2)
    end = clock()
    print 'Multiplication took ',end-start,' seconds'
 
def profile_mult(matrix1,matrix2):
    # A more detailed timing with process information
    # Arguments must be strings for this function
    # eg. profile_mult('a','b')
    cProfile.run('matrix.mult(' + matrix1 + ',' + matrix2 + ')')

def transpose(matrix):
        new_matrix = zero(len(matrix[0]),len(matrix))
        for i in range(len(matrix)):
        	for j in range(len(matrix[0])):
                	new_matrix[j][i] = matrix[i][j]
        return new_matrix

def c_mult(matrix, c):
        new_matrix = zero(len(matrix),len(matrix[0]))
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        new_matrix[i][j] = c*matrix[i][j]
        return new_matrix

def column(matrix, n):
        return transpose([transpose(matrix)[n]])

def mean(matrix):
        new_matrix = zero(len(matrix), 1)           
        norm = 1.0/len(matrix[0])
        for i in range(len(matrix[0])):                 
                new_matrix = add(new_matrix,column(matrix,i))
        return c_mult(new_matrix,norm)

def covariance(matrix):
        m = mean(matrix)
        new_matrix = zero(len(matrix),len(matrix))
        for i in range(len(matrix[0])):
                xn = column(matrix,i)
                variance = add(xn, negate(m))
                new_matrix = add(mult(variance, transpose(variance)),new_matrix)
        return c_mult(new_matrix,(1.0/(len(matrix[0]))))                                         

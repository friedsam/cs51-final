
import string
from numpy import *
from scipy import *

#read data file into array
def readData(file,columns):
        data = fromfile(file,dtype=float, sep = '\n')
        data.resize((data.shape[0]/columns),columns)
        return data

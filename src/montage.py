from numpy import *
import sys
import pickle
import pylab

c_fileInput, c_fileOutput = sys.argv[1:3]


def montage(data, outfile, colormap=pylab.cm.gist_gray):
	dim,numdata = data.shape
	size = sqrt(dim)
	rows = int(ceil(sqrt(numdata)))
	cols = rows
	montageMatrix = zeros((size * rows, size * cols))

	image_id = 0
	for i in range(rows):
		for j in range(cols):
			if image_id >= numdata:
				break
			number = data[:,image_id]
			sliceRow, sliceCol = i * size, j * size
			montageMatrix[sliceRow:sliceRow + size, sliceCol:sliceCol + size] = number.reshape(size,size)
			image_id += 1

	pylab.imshow(montageMatrix, cmap=colormap)
	pylab.axis('off')
	pylab.savefig(outfile)

	return montageMatrix



if __name__ == "__main__":
	pkl = pickle.load(open(c_fileInput))
	montage(pkl, c_fileOutput)

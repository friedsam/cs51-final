from numpy import *
import sys
import pickle
import pylab
import matplotlib.colors as mc

def montage(data, outfile, colormap=pylab.cm.gist_gray):
	# gather information on input data
	dim,numdata = data.shape
	size = sqrt(dim)

	# determine dimensions for array, initialize montageMatrix
	rows = int(ceil(sqrt(numdata)))
	cols = rows
	montageMatrix = zeros((size * rows, size * cols))

	# iterate through data, add each digit to the montage
	image_id = 0
	for i in range(rows):
		for j in range(cols):
			if image_id >= numdata:
				break
			number = data[:,image_id]
			sliceRow, sliceCol = i * size, j * size
			montageMatrix[sliceRow:sliceRow + size, sliceCol:sliceCol + size] = number.reshape(size,size)
			image_id += 1

	# generate image and save to designated outfile
	pylab.imshow(montageMatrix, cmap=colormap)
	pylab.axis('off')
	pylab.savefig(outfile, figsize = (8,8), dpi=100)

	return montageMatrix

def run( inputFilepath, outputFilepath ):
    pkl = pickle.load(open(inputFilepath))
    montage(pkl, outputFilepath)

"""
if __name__ == "__main__":
	pkl = pickle.load(open(c_fileInput))
	montage(pkl, c_fileOutput)

"""

# information for montage digit colors
tp_color = 170.
tp_range = 70.
fn_color = 15.
fn_range = 70.
fp_color = 90.
fp_range = 70.
max_color = 255.

def colorsMontage(data, outfile, colormap=pylab.cm.gnuplot2, normalize=mc.Normalize(vmin=0,vmax=255)):
        # gather information on data
	numdata = len(data)
	dim = len(data[0][0])
	size = sqrt(dim)
	if size % 1 != 0:
		raise Exception("Data not square")

	# determine size of montageMatrix; initialize
	rows = int(ceil(sqrt(numdata)))
	cols = rows
	montageMatrix = zeros((size * rows, size * cols))

	# initialize variables
	image_id = 0
	new_color = 0
	color_range = 0

	for i in range(numdata):
		if image_id >= numdata:
			break
		
		# set data color according TP/FP/FN
		if data[i][1] == "TP":
			new_color = tp_color
			color_range = tp_range
		elif data[i][1] == "FP":
			new_color = fp_color
			color_range = fp_range
		else:
			new_color = fn_color
			color_range = fn_range

		# prepare section of matrix, grab data point
		sliceRow, sliceCol = (image_id / rows) * size, (image_id % cols) * size
		number = array(data[i][0])

                # recolor the number based on true pos / false pos / false neg
                for j in range(dim):
                        if number[j] != 0:
                                number[j] = ((number[j] / max_color) * color_range) + new_color

                # add the number to the montage
                montageMatrix[sliceRow:sliceRow + size, sliceCol:sliceCol + size] = number.reshape(size,size)

                image_id += 1

	# create image and save it to designated outfile
       	pylab.imshow(montageMatrix, cmap=colormap, norm=normalize, interpolation='bicubic')
       	pylab.axis('off')
       	pylab.savefig(outfile)

        return montageMatrix



	"""# gather information on input data
	dim = len(data[0][0])
        numdata = len(data)
        size = sqrt(dim)

	# initialize counting variables
        assigned = 0
        missed = 0

	# determine number of digits to be displayed in the montage
        for i in range(numdata):
                if data[i][2] == digit:
                        assigned += 1
                elif data[i][1] == digit:
                        missed += 1
        total = assigned + missed

	# determine dimensions of the montage, generate the montageMatrix
        rows = int(ceil(sqrt(total)))
        cols = rows
        montageMatrix = zeros((size * rows, size * cols))

	# initialize variables
        image_id = 0
        current_row = 0
        current_column = 0
        new_color = 0
        color_range = 0

	# look at each data point
        for i in range(numdata):

                # if it is actually the given digit
                if data[i][1] == digit:
                        # see if the algorithm identified it correctly, if so, set color to true positive color
                        if data[i][2] == digit:
                                new_color = tp_color
                                color_range = tp_range
                        # otherwise we didn't catch it, set color to false negative color
                        else:
                                new_color = fn_color
                                color_range = fn_range

                # see what else we identified as the digit, but actually isn't, set color to false positive color
                elif data[i][2] == digit:
                        new_color = fp_color
                        color_range = fp_range

                # skip to next iteration for true negatives
                else:
                        continue

		# prepare section of matrix for number; grab data point
		sliceRow, sliceCol = (current_row / rows) * size, (current_column % cols) * size
                number = array(data[i][0])

                # recolor the number based on true pos / false pos / false neg
                for j in range(dim):
                        if number[j] != 0:
                                number[j] = ((number[j] / max_color) * color_range) + new_color

                # add the number to the montage
                montageMatrix[sliceRow:sliceRow + size, sliceCol:sliceCol + size] = number.reshape(size,size)

                # if something was added to the matrix, increment row and column
                current_row += 1
                current_column += 1

	# create image and save it to designated outfile
        pylab.imshow(montageMatrix, cmap=colormap, norm=normalize, interpolation=None)
        pylab.axis('off')
        pylab.savefig(outfile)

	return montageMatrix"""

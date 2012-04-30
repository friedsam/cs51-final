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
	pylab.imsave(fname=outfile, arr=montageMatrix, cmap=colormap, dpi=100, format="png")

	return montageMatrix

def run( inputFilepath, outputFilepath ):
    pkl = pickle.load(open(inputFilepath))
    montage(pkl, outputFilepath)


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
       	pylab.imsave(fname=outfile, arr=montageMatrix, cmap=colormap, vmin=0, vmax=255, dpi=100, format="png") # norm=normalize, interpolation=None, 
    	
	# imgshow not supported in GUI mode
       	# pylab.imshow(montageMatrix, cmap=colormap, norm=normalize, interpolation='bicubic')

        return montageMatrix


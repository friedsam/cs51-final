# cs51-final
Spring 2012 CS51 final project


*----------------------------------------* 
      Feature Extraction and Inference
	for Handwriting Recognition  
		Ver 0.1
		 CS 51
	   Harvard University 
*----------------------------------------*

Authors: 
Yo Sup "Joseph" Moon, 
Dana Modzelewski, 
Claudia Friedsam, and 
William Chambers. 

Submission Date: April 29th, 2012 

This is a toolkit designed to conduct 
feature extraction and clustering on high-dimensional 
data. The canonical example tested was the problem 
of handwriting recognition. 
We ran Principal Component Analysis (PCA) 
and K-means clustering to extract low-dimensional 
feature representation for handwritten digits (0-9) 
and inferred the labels for the test set by using 
Euclidean distance as a metric for closeness.  

Languages: 
Python 

Libraries:
Numpy 
PyQt 

Instructions to run:
There are two ways to run our pipeline. 
We implemented a graphical user interface using PyQt,
but there also exists an easy command-line version. 

>>> GUI Mode:
You need PyQt to run our script with a graphical user interface. 

(1) Run the parse.sh script (sh parse.sh) in the command line 
to parse the text files into pkl format. 
Look at the command line mode instructions for further detail 
for this script.   

(2) run gui.py in the code directory. 
This will launch a GUI window. 

(3) Hit return on the Data path. 
Find directory that contains the pickle files generated by 
the above step (1). 

(4) This provides the data in the "Training Data" and 
"Input Data" section. Choose both. 

(5) Decide which algorithm to run. You can pick 
PCA only, K-means only, or a combination of the both. 
Choose number of principal components and the number of clusters. 

(6) Hit run. In the Results file, pick results. 
This will show a montage. Browse through different images.
If you run supervised learning, this will produce a confusion matrix 
on the lower right side. 

N.B. The confusion matrix is defined as C_{i,j} such that 
C_{1,1} = TP, C_{1,2} = FN, C_{2,1} = FP, C_{2,2} = TN. 
  

>>> Command Line Mode: 
For ease of use, we have 2 shell scripts that 
execute the main functionality of our code.
It is important to run the scripts IN ORDER.
 
(1) runparse.sh: This is a shortcut to run the 
parse_input.py script. Parse_input.py was written 
in a general enough fashion to account for all 
types of text data, given that it is in the following format:

#n
x1 x2 x3 ... 
y1 y2 y3 ...
...
...

The script parses the text data in the data directory 
and coverts them into native numpy arrays. Each column in the 
array corresponds to a data point (i.e. vector representation 
of the handwriting image matrix). The array representation 
is in turn saved as pickle files for easy access and 
reproducibility in the future. 

OR run in command line:
python `pwd`/code/parse_input.py `pwd`/data/handwriting/*.txt 

This takes all the txt files in the handwriting data directory 
and makes pkl files with the same name. 
 
(2) runall.sh: This script executes main.py, which 
executes our main pipeline, given that we have all 
the necessary data provided by the parsing above. 
Running the shell script executes 

python `pwd`/code/main.py `pwd`/data/handwriting/training-9k_colmat.pkl 
`pwd`/data/handwriting/test-1k_colmat.pkl `pwd`/output/ k D. 

The script main.py takes as input arguments 
(1) Pickle to be used as training set
(2) Pickle to be used as test set 
(3) The directory where you want to save the outputted pickle and jpg files
(4) k = number of clusters in k-means 
(5) D = number of principal components in PCA.
  
The shell script runall.sh is initialized with the values 
k=3 and D=10, which we experimentally found to be optimal 
in the time/accuracy tradeoff. 

Output:
The output files are the pickle files containing the assignment 
information for each digit in the test set, and the corresponding 
montage files for each digit class (0-9). These are saved 
in the output folder. For the jpg montage files, the 
yellow digits correspond to true positives, pink to false positives, 
and blue to false negatives. The pickle files contain a triple 
(v, a1, a2) such that v is the digit in array representation, 
a1 is the true label and a2 is the assigned label by our pipeline. 
 

END README 

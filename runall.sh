#!/bin/sh 

#This files runs the entire pca pipeline to produce the results 
#in the output directory. 

#main.py takes 5 input arguments:
#(1) training pickle, (2) test pickle, (3) Output directory (4) value of K in k-means clustering. By trivial consequence, k=0 implies NO k-means. (5) D the number of principal components.  

echo "Running Handwriting Recognition Module ...\n"


echo "Running pca ...\n" 

python `pwd`/code/main.py `pwd`/data/handwriting/training-9k_colmat.pkl `pwd`/data/handwriting/test-1k_colmat.pkl `pwd`/output/ 3 10

echo "Done. \n"

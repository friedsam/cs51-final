#!/bin/sh 
#This files runs the entire pca pipeline to produce the results 
#in the output directory. Right now it is all controlled by 
#this shell script. Maybe in the future we will
#replace this by an SConstruct type build. 

echo "Running Handwriting Recognition Module ..."


echo "Running pca ... "
python src/pca/pca.py data/handwriting/tmp/training-9k_colmat.pkl pca_output.pkl 100

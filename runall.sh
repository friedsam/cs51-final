#!/bin/sh 
#This files runs the entire pca pipeline to produce the results 
#in the output directory. Right now it is all controlled by 
#this shell script. Maybe in the future we will
#replace this by an SConstruct type build. 

#main.py takes 5 input arguments:
#(1) training pickle, (2) test pickle, (3) Output directory (4) value of K in k-means clustering. By trivial consequence, k=0 implies NO k-means. (5) D the number of principal components.  

echo "Running Handwriting Recognition Module ...\n"


echo "Running pca ...\n" 

#python src/main.py /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/training-9k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/test-1k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/output/ 3 10

python src/main.py /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/training-9k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/validation-1k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/output/ 3 10

echo "Done. \n"

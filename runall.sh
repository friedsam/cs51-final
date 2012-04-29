#!/bin/sh 
#This files runs the entire pca pipeline to produce the results 
#in the output directory. Right now it is all controlled by 
#this shell script. Maybe in the future we will
#replace this by an SConstruct type build. 

echo "Running Handwriting Recognition Module ...\n"


echo "Running pca ...\n" 

python src/main.py /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/training-9k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/data/handwriting/test-1k_colmat.pkl /Users/ysupmoon/Documents/cs_51/final_project/cs51-final/output/triple_new.pkl 1 50

echo "Done. \n"

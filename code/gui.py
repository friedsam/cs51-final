#!/usr/bin/env python
# encoding: utf-8
"""
gui.py

Created by Claudia on 2012-04-27.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import string
from numpy import *
import os
import parse_input as ToPickle
import gui_main as ToColmat
import main as PCA
import simplekmeans as KMeans
import pickle
from PyQt4 import QtCore, QtGui
from mainwindow import Ui_MainWindow


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dataPath = None
        self.ui.imageView.setHorizontalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )
        self.ui.imageView.setVerticalScrollBarPolicy( QtCore.Qt.ScrollBarAlwaysOff )

        #QtCore.QObject.connect(self.ui.processDataButton, QtCore.SIGNAL("clicked()"), self.processData)
        QtCore.QObject.connect(self.ui.pcaOnlyCheckbox, QtCore.SIGNAL("clicked()"), self.setPcaOnly)
        QtCore.QObject.connect(self.ui.kmeansOnlyCheckbox, QtCore.SIGNAL("clicked()"), self.setKmeansOnly)
        QtCore.QObject.connect(self.ui.runButton, QtCore.SIGNAL("clicked()"), self.runData)
        QtCore.QObject.connect(self.ui.dataPath, QtCore.SIGNAL("returnPressed()"), self.setDataPath)
        QtCore.QObject.connect(self.ui.resultsFile, QtCore.SIGNAL("currentIndexChanged(int)"), self.setResultsPath)
        QtCore.QObject.connect(self.ui.digit, QtCore.SIGNAL("currentIndexChanged(int)"), self.setDigit)
    
    def processData(self):
        sourceFilepath = QtGui.QFileDialog.getOpenFileName(self, "Select data file", "", "*.txt")
        if os.path.isfile(sourceFilepath):
            destinationPath = None
            if self.dataPath:
                destinationPath = self.dataPath + "/"
            else:
                destinationPath = "./"
            destinationFilename = QtCore.QString(sourceFilepath).replace(QtCore.QRegExp(".*/"), "")
            print("DestinationPath: %s" % destinationPath)
            print("DestinationFilename: %s" % destinationFilename)
            
            ToPickle.parse( str(sourceFilepath), str(destinationPath + destinationFilename.replace(".txt", ".pkl")) )
            ToColmat.parse( str(destinationPath + destinationFilename), str(destinationPath + destinationFilename.replace(".pkl", "_colmat.pkl")) )
            self.ui.dataSet.addItem(destinationFilename)
            self.ui.trainingSet.addItem(destinationFilename)
            
    def setDataPath(self):
        self.dataPath = QtGui.QFileDialog.getExistingDirectory(self, "Select directory", "", QtGui.QFileDialog.ShowDirsOnly)
        self.ui.dataPath.insert(self.dataPath)

        self.updateDataSets()
        self.updateResults()
    
    def setPcaOnly(self):
        self.ui.kmeansOnlyCheckbox.setChecked(False)
    
    def setKmeansOnly(self):
        self.ui.pcaOnlyCheckbox.setChecked(False)
    
    def runData(self):
        if self.ui.pcaOnlyCheckbox.isChecked():
            self.runPcaOnly()
        elif self.ui.kmeansOnlyCheckbox.isChecked():
            self.runKmeansOnly()
        else:
            self.runCombination()
    
    def runPcaOnly(self):
        print("Running PCA Only...")
        inputFilepath  = self.dataPath + "/" + self.ui.dataSet.currentText()
        inputTrainingFilepath  = self.dataPath + "/" + self.ui.trainingSet.currentText()
        outputFilepath = QtCore.QString(inputFilepath).replace("_colmat.pkl", "_result_pca.pkl")
        outputDirpath  = QtCore.QString(outputFilepath).replace(".pkl", "")
        QtCore.QDir().mkdir(outputDirpath)
        PCA.run( str(inputFilepath), str(inputTrainingFilepath), str(outputFilepath), str(outputDirpath), 1, self.ui.pcaNumComp.value() )
        self.updateResults()
    
    def runKmeansOnly(self):
        print("Running K-Means Only...")
        inputFilepath  = self.dataPath + "/" + self.ui.trainingSet.currentText()
        outputFilepath = QtCore.QString(inputFilepath).replace("_colmat.pkl", "_result_kmeans.pkl")
        outputDirpath  = QtCore.QString(outputFilepath).replace(".pkl", "")
        QtCore.QDir().mkdir(outputDirpath)
        KMeans.run( str(inputFilepath), str(outputFilepath), str(outputDirpath), self.ui.kmeansNumClust.value() )
        self.updateResults()
    
    def runCombination(self):
        print("Running Combination...")
        inputFilepath  = self.dataPath + "/" + self.ui.dataSet.currentText()
        inputTrainingFilepath  = self.dataPath + "/" + self.ui.trainingSet.currentText()
        outputFilepath = QtCore.QString(inputFilepath).replace("_colmat.pkl", "_result_combination.pkl")
        outputDirpath  = QtCore.QString(outputFilepath).replace(".pkl", "")
        QtCore.QDir().mkdir(outputDirpath)
        PCA.run( str(inputFilepath), str(inputTrainingFilepath), str(outputFilepath), str(outputDirpath), self.ui.kmeansNumClust.value(), self.ui.pcaNumComp.value() )
        self.updateResults()

    def updateDataSets(self):
        filelist = QtCore.QDir(self.dataPath).entryList()
        self.ui.dataSet.clear()
        self.ui.dataSet.addItems(filelist.filter("_colmat.pkl"))
        self.ui.trainingSet.clear()
        self.ui.trainingSet.addItems(filelist.filter("_colmat.pkl"))

    def updateResults(self):
        dirlist = QtCore.QDir(self.dataPath).entryList(QtCore.QDir.Dirs)
        self.ui.resultsFile.clear()
        self.ui.resultsFile.addItems(dirlist.filter("result"))
        self.updateDigits()
    
    def setResultsPath(self, value):
        self.updateDigits()
        
    def updateDigits(self):
        self.digitsPath = QtCore.QString(self.dataPath + "/" + self.ui.resultsFile.currentText())

        filelist = QtCore.QDir(self.digitsPath).entryList()
        self.ui.digit.clear()
        self.ui.digit.addItems(filelist.filter(".png"))
    
    def setDigit(self):
        imageFilepath = QtCore.QString(self.digitsPath + "/" + self.ui.digit.currentText())
        print("Selected Image: %s" % imageFilepath)

        if os.path.isfile(imageFilepath):
            img = QtGui.QImage(imageFilepath)
            pixMap = QtGui.QPixmap.fromImage(img)

            scene = QtGui.QGraphicsScene()
            self.ui.imageView.setScene(scene)
            pixMap = pixMap.scaled(self.ui.imageView.size())
            scene.clear()
            scene.addPixmap(pixMap)
            self.ui.imageView.repaint()
            self.ui.imageView.show()
            print("Image updated")
            self.updateConfusion()
        else:
            scene = QtGui.QGraphicsScene()
            self.ui.imageView.setScene(scene)
            scene.clear()
            self.ui.imageView.repaint()
            self.ui.imageView.show()
            print("No Image file found")
    
    def updateConfusion(self):
        filepath = self.digitsPath + "/conf_" + self.ui.digit.currentText().replace(".png", ".pkl")
        print("filepath %s" % filepath)
        confusionData = pickle.load(open(filepath))[1]
      
        cell1 = QtGui.QTableWidgetItem(str(confusionData[0][0]))
        cell1.setBackground(QtGui.QBrush(QtGui.QColor( 0, 255, 0, 100 )))
        cell1.setTextAlignment(QtCore.Qt.AlignCenter)
        cell2 = QtGui.QTableWidgetItem(str(confusionData[0][1]))
        cell2.setBackground(QtGui.QBrush(QtGui.QColor( 255, 0, 0, 100 )))
        cell2.setTextAlignment(QtCore.Qt.AlignCenter)
        cell3 = QtGui.QTableWidgetItem(str(confusionData[1][0]))
        cell3.setBackground(QtGui.QBrush(QtGui.QColor( 255, 0, 0, 100 )))
        cell3.setTextAlignment(QtCore.Qt.AlignCenter)
        cell4 = QtGui.QTableWidgetItem(str(confusionData[1][1]))
        cell4.setBackground(QtGui.QBrush(QtGui.QColor( 0, 255, 0, 100 )))
        cell4.setTextAlignment(QtCore.Qt.AlignCenter)
        
        self.ui.confusion.setItem(0,0, cell1)
        self.ui.confusion.setItem(0,1, cell2)
        self.ui.confusion.setItem(1,0, cell3)
        self.ui.confusion.setItem(1,1, cell4)
        
        print("Updating confusion to: %s" % filepath)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Apr 29 20:27:49 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(957, 607)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 301, 551))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 151, 51))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dataPathLabel = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dataPathLabel.setFont(font)
        self.dataPathLabel.setObjectName(_fromUtf8("dataPathLabel"))
        self.verticalLayout.addWidget(self.dataPathLabel)
        self.dataPath = QtGui.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dataPath.setFont(font)
        self.dataPath.setText(_fromUtf8(""))
        self.dataPath.setObjectName(_fromUtf8("dataPath"))
        self.verticalLayout.addWidget(self.dataPath)
        self.dataSet = QtGui.QComboBox(self.groupBox)
        self.dataSet.setGeometry(QtCore.QRect(10, 180, 281, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dataSet.setFont(font)
        self.dataSet.setObjectName(_fromUtf8("dataSet"))
        self.dataSetLabel = QtGui.QLabel(self.groupBox)
        self.dataSetLabel.setGeometry(QtCore.QRect(10, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.dataSetLabel.setFont(font)
        self.dataSetLabel.setObjectName(_fromUtf8("dataSetLabel"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pcaOnlyCheckbox = QtGui.QCheckBox(self.groupBox)
        self.pcaOnlyCheckbox.setGeometry(QtCore.QRect(140, 240, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pcaOnlyCheckbox.setFont(font)
        self.pcaOnlyCheckbox.setObjectName(_fromUtf8("pcaOnlyCheckbox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 270, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pcaNumComp = QtGui.QSpinBox(self.groupBox)
        self.pcaNumComp.setGeometry(QtCore.QRect(20, 290, 57, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pcaNumComp.setFont(font)
        self.pcaNumComp.setObjectName(_fromUtf8("pcaNumComp"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 350, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.kmeansOnlyCheckbox = QtGui.QCheckBox(self.groupBox)
        self.kmeansOnlyCheckbox.setGeometry(QtCore.QRect(140, 350, 87, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kmeansOnlyCheckbox.setFont(font)
        self.kmeansOnlyCheckbox.setObjectName(_fromUtf8("kmeansOnlyCheckbox"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 380, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.kmeansNumClust = QtGui.QSpinBox(self.groupBox)
        self.kmeansNumClust.setGeometry(QtCore.QRect(20, 400, 57, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.kmeansNumClust.setFont(font)
        self.kmeansNumClust.setObjectName(_fromUtf8("kmeansNumClust"))
        self.runButton = QtGui.QPushButton(self.groupBox)
        self.runButton.setGeometry(QtCore.QRect(90, 480, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.runButton.setFont(font)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.trainingSet = QtGui.QComboBox(self.groupBox)
        self.trainingSet.setGeometry(QtCore.QRect(10, 130, 281, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.trainingSet.setFont(font)
        self.trainingSet.setObjectName(_fromUtf8("trainingSet"))
        self.trainingSetLabel = QtGui.QLabel(self.groupBox)
        self.trainingSetLabel.setGeometry(QtCore.QRect(10, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.trainingSetLabel.setFont(font)
        self.trainingSetLabel.setObjectName(_fromUtf8("trainingSetLabel"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 20, 601, 551))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.resultsFile = QtGui.QComboBox(self.groupBox_2)
        self.resultsFile.setGeometry(QtCore.QRect(20, 60, 271, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.resultsFile.setFont(font)
        self.resultsFile.setObjectName(_fromUtf8("resultsFile"))
        self.digit = QtGui.QComboBox(self.groupBox_2)
        self.digit.setGeometry(QtCore.QRect(430, 280, 141, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.digit.setFont(font)
        self.digit.setObjectName(_fromUtf8("digit"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(430, 260, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.imageView = QtGui.QGraphicsView(self.groupBox_2)
        self.imageView.setGeometry(QtCore.QRect(20, 120, 401, 401))
        self.imageView.setObjectName(_fromUtf8("imageView"))
        self.confusion = QtGui.QTableWidget(self.groupBox_2)
        self.confusion.setGeometry(QtCore.QRect(440, 380, 151, 141))
        self.confusion.setShowGrid(True)
        self.confusion.setCornerButtonEnabled(True)
        self.confusion.setRowCount(2)
        self.confusion.setColumnCount(2)
        self.confusion.setObjectName(_fromUtf8("confusion"))
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.confusion.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.confusion.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.confusion.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255, 69))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        self.confusion.setItem(1, 1, item)
        self.confusion.horizontalHeader().setVisible(False)
        self.confusion.horizontalHeader().setCascadingSectionResizes(False)
        self.confusion.horizontalHeader().setDefaultSectionSize(74)
        self.confusion.verticalHeader().setVisible(False)
        self.confusion.verticalHeader().setDefaultSectionSize(69)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Data Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.dataPathLabel.setText(QtGui.QApplication.translate("MainWindow", "Data Path", None, QtGui.QApplication.UnicodeUTF8))
        self.dataSetLabel.setText(QtGui.QApplication.translate("MainWindow", "Input Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "PCA", None, QtGui.QApplication.UnicodeUTF8))
        self.pcaOnlyCheckbox.setText(QtGui.QApplication.translate("MainWindow", "Only", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Nr of Principal Components:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "K-Means", None, QtGui.QApplication.UnicodeUTF8))
        self.kmeansOnlyCheckbox.setText(QtGui.QApplication.translate("MainWindow", "Only", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Nr of Clusters:", None, QtGui.QApplication.UnicodeUTF8))
        self.runButton.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.trainingSetLabel.setText(QtGui.QApplication.translate("MainWindow", "Training Data", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Digit / Cluster", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Results File", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.confusion.isSortingEnabled()
        self.confusion.setSortingEnabled(False)
        self.confusion.setSortingEnabled(__sortingEnabled)


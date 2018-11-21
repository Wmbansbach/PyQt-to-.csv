# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\remov\Desktop\RBWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(348, 361)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Documents/Icons/Banana.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(220, 220, 220);")
        MainWindow.setIconSize(QtCore.QSize(15, 15))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.primaryValuesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.primaryValuesBox.setEnabled(False)
        self.primaryValuesBox.setGeometry(QtCore.QRect(120, 60, 211, 121))
        self.primaryValuesBox.setStyleSheet("background-color: rgb(212, 255, 255);")
        self.primaryValuesBox.setObjectName("primaryValuesBox")

        self.dateLabel = QtWidgets.QLabel(self.primaryValuesBox)
        self.dateLabel.setGeometry(QtCore.QRect(10, 30, 51, 16))
        self.dateLabel.setObjectName("dateLabel")

        self.amtLabel = QtWidgets.QLabel(self.primaryValuesBox)
        self.amtLabel.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.amtLabel.setObjectName("amtLabel")

        self.gasLabel = QtWidgets.QLabel(self.primaryValuesBox)
        self.gasLabel.setGeometry(QtCore.QRect(10, 90, 47, 13))
        self.gasLabel.setObjectName("gasLabel")

        self.dateEdit = QtWidgets.QLineEdit(self.primaryValuesBox)
        self.dateEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.dateEdit.setAutoFillBackground(False)
        self.dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dateEdit.setObjectName("dateEdit")

        self.amtEdit = QtWidgets.QLineEdit(self.primaryValuesBox)
        self.amtEdit.setGeometry(QtCore.QRect(80, 60, 113, 20))
        self.amtEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.amtEdit.setObjectName("amtEdit")

        self.gasEdit = QtWidgets.QLineEdit(self.primaryValuesBox)
        self.gasEdit.setGeometry(QtCore.QRect(80, 90, 113, 20))
        self.gasEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gasEdit.setObjectName("gasEdit")

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.StartButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.StartButton.setObjectName("StartButton")

        self.StartButton.clicked.connect(self.OnStartClick)
        self.ExtraExpensesBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ExtraExpensesBox.setEnabled(False)
        self.ExtraExpensesBox.setGeometry(QtCore.QRect(120, 200, 211, 121))
        self.ExtraExpensesBox.setStyleSheet("background-color: rgb(212, 255, 255);")
        self.ExtraExpensesBox.setObjectName("ExtraExpensesBox")

        self.nameLabel = QtWidgets.QLabel(self.ExtraExpensesBox)
        self.nameLabel.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.nameLabel.setObjectName("nameLabel")

        self.valueLabel = QtWidgets.QLabel(self.ExtraExpensesBox)
        self.valueLabel.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.valueLabel.setObjectName("valueLabel")

        self.lineEdit = QtWidgets.QLineEdit(self.ExtraExpensesBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.ExtraExpensesBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.submitButton = QtWidgets.QPushButton(self.ExtraExpensesBox)
        self.submitButton.setGeometry(QtCore.QRect(60, 90, 75, 23))
        self.submitButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.OnSubmitClick)

        self.ExtraExpButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExtraExpButton.setEnabled(False)
        self.ExtraExpButton.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.ExtraExpButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ExtraExpButton.setObjectName("ExtraExpButton")
        self.ExtraExpButton.clicked.connect(self.OnEEClick)

        self.DoneButton = QtWidgets.QPushButton(self.centralwidget)
        self.DoneButton.setEnabled(False)
        self.DoneButton.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.DoneButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DoneButton.setObjectName("DoneButton")
        self.DoneButton.clicked.connect(self.OnDoneClick)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 348, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shells Tax App"))
        self.primaryValuesBox.setTitle(_translate("MainWindow", "Normal Values"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.amtLabel.setText(_translate("MainWindow", "Check Amt"))
        self.gasLabel.setText(_translate("MainWindow", "Gas"))
        self.StartButton.setText(_translate("MainWindow", "Start"))
        self.ExtraExpensesBox.setTitle(_translate("MainWindow", "Extra Expenses"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.valueLabel.setText(_translate("MainWindow", "Value"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.ExtraExpButton.setText(_translate("MainWindow", "Extras?"))
        self.DoneButton.setText(_translate("MainWindow", "Finish"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 761, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MainGridLayOut = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MainGridLayOut.setContentsMargins(0, 0, 0, 0)
        self.MainGridLayOut.setObjectName("MainGridLayOut")
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuVersion = QtWidgets.QMenu(self.menubar)
        self.menuVersion.setObjectName("menuVersion")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuVersion.menuAction())

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "MainWindow"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuEdit.setTitle(_translate("MainForm", "Edit"))
        self.menuAbout.setTitle(_translate("MainForm", "About"))
        self.menuVersion.setTitle(_translate("MainForm", "Version"))


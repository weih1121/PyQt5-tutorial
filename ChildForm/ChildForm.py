# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildForm(object):
    def setupUi(self, ChildForm):
        ChildForm.setObjectName("ChildForm")
        ChildForm.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ChildForm)
        self.centralwidget.setObjectName("centralwidget")
        ChildForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChildForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        ChildForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChildForm)
        self.statusbar.setObjectName("statusbar")
        ChildForm.setStatusBar(self.statusbar)

        self.retranslateUi(ChildForm)
        QtCore.QMetaObject.connectSlotsByName(ChildForm)

    def retranslateUi(self, ChildForm):
        _translate = QtCore.QCoreApplication.translate
        ChildForm.setWindowTitle(_translate("ChildForm", "MainWindow"))


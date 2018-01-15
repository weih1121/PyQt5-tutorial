# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuBar&ToolBar.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Edit = QtWidgets.QMenu(self.menubar)
        self.Edit.setObjectName("Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.CreateNewFileAction = QtWidgets.QAction(MainWindow)
        self.CreateNewFileAction.setObjectName("CreateNewFileAction")
        self.NewFileAction = QtWidgets.QAction(MainWindow)
        self.NewFileAction.setObjectName("NewFileAction")
        self.CloseFileAction = QtWidgets.QAction(MainWindow)
        self.CloseFileAction.setObjectName("CloseFileAction")
        self.File.addAction(self.CreateNewFileAction)
        self.File.addAction(self.NewFileAction)
        self.File.addAction(self.CloseFileAction)
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Edit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.File.setTitle(_translate("MainWindow", "文件(&F)"))
        self.Edit.setTitle(_translate("MainWindow", "编辑(&E)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.CreateNewFileAction.setText(_translate("MainWindow", "新建"))
        self.CreateNewFileAction.setToolTip(_translate("MainWindow", "新建"))
        self.CreateNewFileAction.setShortcut(_translate("MainWindow", "Ctrl+Shift+O"))
        self.NewFileAction.setText(_translate("MainWindow", "打开"))
        self.NewFileAction.setToolTip(_translate("MainWindow", "dakai"))
        self.NewFileAction.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.CloseFileAction.setText(_translate("MainWindow", "关闭"))
        self.CloseFileAction.setToolTip(_translate("MainWindow", "关闭"))
        self.CloseFileAction.setShortcut(_translate("MainWindow", "Ctrl+S"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Group.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag


class button(QPushButton):
    def __init__(self):
        super(button, self).__init__()

        def mouseMoveEvent(self, e):

            if e.buttons() != Qt.RightButton:
                return

            mimeData = QMimeData()

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(e.pos() - self.rect().topLeft())

            dropAction = drag.exec_(Qt.MoveAction)

        def mousePressEvent(self, e):

            super().mousePressEvent(e)

            if e.button() == Qt.LeftButton:
                print('press')






class Ui_Form(QtWidgets):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1400, 750)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(40, 20, 681, 481))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 679, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_students = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_students.setWidgetResizable(True)
        self.scrollArea_students.setObjectName("scrollArea_students")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 323, 455))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setGeometry(QtCore.QRect(30, 50, 211, 170))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_student1 = QtWidgets.button(self.widget)
        self.pushButton_student1.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student1.setObjectName("pushButton_student1")
        self.gridLayout.addWidget(self.pushButton_student1, 0, 0, 1, 1)
        self.pushButton_student2 = QtWidgets.button(self.widget)
        self.pushButton_student2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student2.setObjectName("pushButton_student2")
        self.gridLayout.addWidget(self.pushButton_student2, 0, 1, 1, 1)
        self.pushButton_student3 = QtWidgets.button(self.widget)
        self.pushButton_student3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student3.setObjectName("pushButton_student3")
        self.gridLayout.addWidget(self.pushButton_student3, 1, 0, 1, 1)
        self.pushButton_student4 = QtWidgets.button(self.widget)
        self.pushButton_student4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student4.setObjectName("pushButton_student4")
        self.gridLayout.addWidget(self.pushButton_student4, 1, 1, 1, 1)
        self.pushButton_student5 = QtWidgets.button(self.widget)
        self.pushButton_student5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student5.setObjectName("pushButton_student5")
        self.gridLayout.addWidget(self.pushButton_student5, 2, 0, 1, 1)
        self.pushButton_student6 = QtWidgets.button(self.widget)
        self.pushButton_student6.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student6.setObjectName("pushButton_student6")
        self.gridLayout.addWidget(self.pushButton_student6, 2, 1, 1, 1)
        self.pushButton_student7 = QtWidgets.button(self.widget)
        self.pushButton_student7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student7.setObjectName("pushButton_student7")
        self.gridLayout.addWidget(self.pushButton_student7, 3, 0, 1, 1)
        self.pushButton_student8 = QtWidgets.button(self.widget)
        self.pushButton_student8.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student8.setObjectName("pushButton_student8")
        self.gridLayout.addWidget(self.pushButton_student8, 3, 1, 1, 1)
        self.pushButton_student9 = QtWidgets.button(self.widget)
        self.pushButton_student9.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student9.setObjectName("pushButton_student9")
        self.gridLayout.addWidget(self.pushButton_student9, 4, 0, 1, 1)
        self.pushButton_student10 = QtWidgets.button(self.widget)
        self.pushButton_student10.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_student10.setObjectName("pushButton_student10")
        self.gridLayout.addWidget(self.pushButton_student10, 4, 1, 1, 1)
        self.scrollArea_students.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_students)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_groupNum = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_groupNum.setObjectName("label_groupNum")
        self.horizontalLayout.addWidget(self.label_groupNum)
        self.spinBox_groupNum = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox_groupNum.setObjectName("spinBox_groupNum")
        self.horizontalLayout.addWidget(self.spinBox_groupNum)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea_3 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 321, 423))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.widget1 = QtWidgets.QWidget(self.scrollAreaWidgetContents_3)
        self.widget1.setGeometry(QtCore.QRect(30, 40, 126, 135))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget1)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 4, 1, 1, 1)
        self.scrollArea_students.raise_()
        self.scrollArea_students.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()
        self.comboBox_5.raise_()
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_student1.setText(_translate("Form", "student1"))
        self.pushButton_student2.setText(_translate("Form", "student2"))
        self.pushButton_student3.setText(_translate("Form", "student3"))
        self.pushButton_student4.setText(_translate("Form", "student4"))
        self.pushButton_student5.setText(_translate("Form", "student5"))
        self.pushButton_student6.setText(_translate("Form", "student6"))
        self.pushButton_student7.setText(_translate("Form", "student7"))
        self.pushButton_student8.setText(_translate("Form", "student8"))
        self.pushButton_student9.setText(_translate("Form", "student9"))
        self.pushButton_student10.setText(_translate("Form", "student10"))
        self.label_groupNum.setText(_translate("Form", "组数"))
        self.label.setText(_translate("Form", "组一"))
        self.comboBox.setItemText(0, _translate("Form", "TeacherWang"))
        self.label_2.setText(_translate("Form", "组二"))
        self.comboBox_2.setItemText(0, _translate("Form", "TeacherWang"))
        self.label_3.setText(_translate("Form", "组三"))
        self.comboBox_3.setItemText(0, _translate("Form", "TeacherWang"))
        self.label_4.setText(_translate("Form", "组四"))
        self.comboBox_4.setItemText(0, _translate("Form", "TeacherWang"))
        self.label_5.setText(_translate("Form", "组五"))
        self.comboBox_5.setItemText(0, _translate("Form", "TeacherWang"))


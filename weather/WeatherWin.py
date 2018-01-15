# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WeatherWin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 436)
        self.pushButtonQuery = QtWidgets.QPushButton(Form)
        self.pushButtonQuery.setGeometry(QtCore.QRect(140, 350, 93, 28))
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.pushButtonClear = QtWidgets.QPushButton(Form)
        self.pushButtonClear.setGeometry(QtCore.QRect(550, 350, 93, 28))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.groupBoxWeatherQuery = QtWidgets.QGroupBox(Form)
        self.groupBoxWeatherQuery.setGeometry(QtCore.QRect(50, 40, 701, 271))
        self.groupBoxWeatherQuery.setObjectName("groupBoxWeatherQuery")
        self.labelCity = QtWidgets.QLabel(self.groupBoxWeatherQuery)
        self.labelCity.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.labelCity.setObjectName("labelCity")
        self.comboBoxWeather = QtWidgets.QComboBox(self.groupBoxWeatherQuery)
        self.comboBoxWeather.setGeometry(QtCore.QRect(90, 20, 401, 22))
        self.comboBoxWeather.setObjectName("comboBoxWeather")
        self.comboBoxWeather.addItem("")
        self.comboBoxWeather.addItem("")
        self.comboBoxWeather.addItem("")
        self.textEditResult = QtWidgets.QTextEdit(self.groupBoxWeatherQuery)
        self.textEditResult.setGeometry(QtCore.QRect(10, 50, 681, 211))
        self.textEditResult.setObjectName("textEditResult")

        self.retranslateUi(Form)
        self.pushButtonQuery.clicked.connect(Form.queryWeather)
        self.pushButtonClear.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButtonQuery.setText(_translate("Form", "查询"))
        self.pushButtonClear.setText(_translate("Form", "清空"))
        self.groupBoxWeatherQuery.setTitle(_translate("Form", "查询城市天气"))
        self.labelCity.setText(_translate("Form", "城市"))
        self.comboBoxWeather.setItemText(0, _translate("Form", "北京"))
        self.comboBoxWeather.setItemText(1, _translate("Form", "上海"))
        self.comboBoxWeather.setItemText(2, _translate("Form", "天津"))



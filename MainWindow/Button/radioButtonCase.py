import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        layout = QHBoxLayout()

        self.btn1 = QRadioButton("Button1")
        self.btn1.setChecked(True)
        self.btn1.clicked.connect(lambda : self.btnstate(self.btn1))

        self.btn2 = QRadioButton("Button2")
        self.btn2.toggled.connect(lambda : self.btnstate(self.btn2))

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)
        self.setWindowTitle("PushButton案例")

    def btnstate(self, btn):
        if btn.text() == "Button1":
            if btn.isChecked() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deseleted")

        if btn.text() == "Button2":
            if btn.isChecked() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deseleted")

    def whichbtn(self, btn):
        print("Check button is" + btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())
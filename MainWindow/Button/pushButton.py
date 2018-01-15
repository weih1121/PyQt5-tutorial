import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        layout = QVBoxLayout()

        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(lambda : self.whichbtn(self.btn1))
        self.btn1.clicked.connect(self.btnstate)

        self.btn2 = QPushButton("Image")
        self.btn2.setIcon(QIcon(QPixmap("./images/quit.png")))
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda : self.whichbtn(self.btn4))



        self.setLayout(layout)
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setWindowTitle("PushButton案例")

    def btnstate(self):
        if self.btn1.isChecked():
            print("Btn1 Pressed!")
        else:
            print("Button Released")

    def whichbtn(self, btn):
        print("Check button is" + btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())
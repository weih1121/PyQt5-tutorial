import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

class myWindow(QWidget):

    def __init__(self):
        super(myWindow, self).__init__()
        self.setWindowTitle("嵌套布局")

        wlayout = QHBoxLayout()

        hlayout = QVBoxLayout()
        vlayout = QVBoxLayout()
        glayout = QGridLayout()
        flayout = QFormLayout()

        self.btn1 = QPushButton(str(1))
        self.btn2 = QPushButton(str(2))
        self.btn3 = QPushButton(str(3))
        self.btn4 = QPushButton(str(4))
        self.btn5 = QPushButton(str(5))
        self.btn6 = QPushButton(str(6))
        self.btn7 = QPushButton(str(7))
        self.btn8 = QPushButton(str(8))
        self.btn9 = QPushButton(str(9))
        self.btn10 = QPushButton(str(10))
        self.btn11 = QPushButton(str(11))
        self.btn12 = QPushButton(str(12))

        hlayout.addWidget(self.btn1)
        hlayout.addWidget(self.btn2)

        vlayout.addWidget(self.btn3)
        vlayout.addWidget(self.btn4)

        glayout.addWidget(self.btn5, 0, 0)
        glayout.addWidget(self.btn6, 0, 1)
        glayout.addWidget(self.btn7, 1, 0)
        glayout.addWidget(self.btn8, 1, 1)

        flayout.addWidget(self.btn9)
        flayout.addWidget(self.btn10)
        flayout.addWidget(self.btn11)
        flayout.addWidget(self.btn12)

        hwg = QWidget()
        vwg = QWidget()
        gwg = QWidget()
        fwg = QWidget()

        hwg.setLayout(hlayout)
        vwg.setLayout(vlayout)
        gwg.setLayout(glayout)
        fwg.setLayout(flayout)

        wlayout.addWidget(hwg)
        wlayout.addWidget(vwg)
        wlayout.addWidget(gwg)
        wlayout.addWidget(fwg)



        self.setLayout(wlayout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = myWindow()
    win.show()
    sys.exit(app.exec_())
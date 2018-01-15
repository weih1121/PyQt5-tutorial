from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys
from functools import partial

class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle("内置信号与槽函数")
        self.resize(300, 500)

        btn = QPushButton("关闭", self)    #
        btn.clicked.connect(self.close)
        btn.move(150, 250)

class WinForm01(QWidget):

    btn_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinForm01, self).__init__()
        self.setWindowTitle("自定义信号与内置槽函数")
        self.resize(300, 300)

        btn = QPushButton('关闭', self)

        btn.clicked.connect(self.btn_clicked)
        self.btn_clicked_signal.connect(self.close)


    def btn_clicked(self):
        self.btn_clicked_signal.emit()

class WinForm02(QWidget):
    btn_clicked_signal = pyqtSignal()

    def __init__(self):
        super(WinForm02, self).__init__()

        self.setWindowTitle("自定义信号与自定义槽")
        self.resize(300, 500)

        btn = QPushButton("关闭", self)
        btn.clicked.connect(self.btn_clicked)
        self.btn_clicked_signal.connect(self.btn_close)


    def btn_clicked(self):
        self.btn_clicked_signal.emit()

    def btn_close(self):
        self.close()


class  WinForm03(QMainWindow):
    def __init__(self):
        super(WinForm03, self).__init__()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")

        #btn1.clicked.connect(lambda: self.onButtonClicked(1))          #第一种使用lambda表达式 传递给槽函数参数
        #btn2.clicked.connect(lambda: self.onButtonClicked(2))

        btn1.clicked.connect(partial(self.onButtonClicked, 1))          #第二种使用functools中的partical函数 为槽函数传递参数
        btn2.clicked.connect(partial(self.onButtonClicked, 2))

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        main_Frame = QWidget()
        main_Frame.setLayout(layout)
        self.setCentralWidget(main_Frame)


    def onButtonClicked(self, n):
        print("Button {0} was Clicked".format(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm03()
    win.show()
    sys.exit(app.exec_())
from MainForm import *
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow, Ui_MainForm):
    def __init__(self,):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
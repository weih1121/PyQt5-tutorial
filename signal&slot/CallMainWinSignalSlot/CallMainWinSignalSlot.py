import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from CallMainWinSignalSlot.MainWinSignalSlot01 import Ui_Form

class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
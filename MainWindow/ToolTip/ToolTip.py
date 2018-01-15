import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont

class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.toolTip = QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')
        self.setGeometry(200, 300, 800, 500)
        self.setWindowTitle('气泡提示demo')

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QMenu, QWidget
from PyQt5.QtCore import QEvent, QTimer, Qt
from PyQt5.QtGui import QPainter

class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.justDoubleClicked = False
        self.Key = ''
        self.text = ''
        self.message = ''
        self.resize(400, 300)
        self.move(100, 100)
        self.setWindowTitle("Events")
        QTimer.singleShot(3000, self.giveHelp)

    def giveHelp(self):
        self.text = '点击这里, 出发鼠标追踪功能'
        self.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = widget()
    win.show()
    sys.exit(app.exec_())
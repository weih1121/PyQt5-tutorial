import sys
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QMainWindow

class WinForm(QMainWindow):
    def __init__(self):
        super(WinForm, self).__init__()

        self.setWindowTitle("窗口放在屏幕中间")
        self.resize(640, 320)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
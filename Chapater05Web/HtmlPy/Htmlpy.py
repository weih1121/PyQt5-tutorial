from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("加载Html网页例子")
        self.setGeometry(5, 30, 555, 300)
        self.browser = QWebEngineView()                 #创建一个webEngineView

        url = r'C:/PythonProject/Chapater05Web/HtmlPy/index.html'
        self.browser.load(QUrl(url))
        self.setCentralWidget(self.browser)             #将webEngine(broswer)放到我们的窗口中间

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
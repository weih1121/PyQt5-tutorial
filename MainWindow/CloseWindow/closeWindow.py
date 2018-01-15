# —*— coding: UTF-8 -*-                                                                #避免在不同操作系统下出现中文乱码


from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QApplication, QWidget
import sys

class WinForm(QMainWindow):
    def __init__(self, parent = None):
        super(WinForm, self).__init__(parent)
        self.setWindowTitle("CloseWindow")
        self.button = QPushButton("关闭窗口")
        self.button.clicked.connect(self.onButtonClicked)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClicked(self):

        #sender = self.sender()
        print(self.button.text() + 'Pushed')
        QApp = QApplication.instance()          #获取本例子中QApplication（）的实例化对象app
        QApp.quit()                             #调用app的quit()函数

if __name__ == "__main__":

        app = QApplication(sys.argv)
        win = WinForm()
        win.show()
        sys.exit(app.exec_())
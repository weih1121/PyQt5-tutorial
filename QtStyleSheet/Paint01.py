import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBitmap

class MyForm(QWidget):
    def __int__(self):
        super(MyForm, self).__int__()
        self.setWindowTitle("不规则窗口实现例子")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, 280, 390, QPixmap(r"./images/2018.jpg"))
        painter.drawPixmap(300, 0, 280, 390, QBitmap(r"./images/2018.jpg"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    sys.exit(app.exec_())
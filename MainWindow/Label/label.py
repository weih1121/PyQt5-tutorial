from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
import sys

class WinDemo(QWidget):
    def __init__(self):
        super(WinDemo, self).__init__()

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("这是一个文本标签")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.red)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href = '#'>欢迎使用Python Gui应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("./images/penguin.png"))
        label4.setText("<A href='http://www.baidu.com'>欢迎访问此处</A>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超链接")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)
        vbox.addStretch()

        label1.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(False)
        label4.linkActivated.connect(self.link_clicked)

        label2.linkHovered.connect(self.link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel")

    def link_hovered(self):
        print("鼠标滑过label2， 触发事件")

    def link_clicked(self):
        print("鼠标点击label4， 触发事件")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinDemo()
    win.show()
    sys.exit(app.exec_())
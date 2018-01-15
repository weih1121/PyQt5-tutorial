import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QComboBox,QMainWindow,QHBoxLayout

class Dialog(QMainWindow):

    def __init__(self):
        super(Dialog, self).__init__()

        self.setAcceptDrops(True)                                   #设置接受拖拽操作

        self.setWindowTitle("DragAndDropWithButtonAndComboBox")
        self.layout = QHBoxLayout()

        self.layout.addWidget(QPushButton("第一个按钮"))
        self.layout.addWidget(QPushButton("第二个按钮"))
        self.layout.addWidget(QPushButton("第三个按钮"))
        self.layout.addWidget(QPushButton("第四个按钮"))

        self.setLayout(self.layout)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())
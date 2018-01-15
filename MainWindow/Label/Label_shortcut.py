from PyQt5.QtWidgets import *
import sys

class QlabelDemo(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel例子")
        nameLb1 = QLabel("&Name", self)
        nameEd1 = QLineEdit(self)
        nameEd1.setEchoMode(QLineEdit.Normal)       #输入什么显示什么
        nameLb1.setBuddy(nameEd1)

        nameLb2 = QLabel("&Passward", self)
        nameEd2 = QLineEdit(self)
        nameEd2.setEchoMode(QLineEdit.Password)     #输入之后是圆点
        nameLb2.setBuddy(nameEd2)

        btnOk = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLb1, 0, 0)
        mainLayout.addWidget(nameEd1, 0, 1, 1, 2)

        mainLayout.addWidget(nameLb2, 1, 0)
        mainLayout.addWidget(nameEd2, 1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    labelDemo = QlabelDemo()
    labelDemo.show()
    sys.exit(app.exec_())
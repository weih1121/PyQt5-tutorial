from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys

class LineEditDemo(QWidget):
    def __init__(self):
        super(LineEditDemo, self).__init__()
        e1 = QLineEdit()
        e1.setValidator( QIntValidator())                   #设置验证器，且输入框内验证的数据类型为int
        e1.setMaxLength(4)                                  #设置验证器数据的最大长度
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))  # 设置验证器，且输入框内验证的数据类型为double

        flo = QFormLayout()
        flo.addRow("interger validator", e1)
        flo.addRow(("double validator"), e2)

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')
        flo.addRow("Input Mask", e3)

        e4 = QLineEdit()
        e4.textChanged.connect(self.textChanged)
        flo.addRow("TextChanged", e4)

        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        flo.addRow("Passward", e5)

        e6 = QLineEdit("Hello")
        e6.setReadOnly(True)
        flo.addRow("Read Only", e6)

        e5.editingFinished.connect(self.press)
        self.setLayout(flo)
        self.setWindowTitle("输入各种不同类型案例")


    def textChanged(self, text):
        print("输入的内容为：" + text)

    def press(self):
        print("已输入值！")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec_())

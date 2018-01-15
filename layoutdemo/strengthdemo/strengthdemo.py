from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
import sys

class WindowDemo(QWidget):
    def __init__(self):
        super(WindowDemo, self).__init__()

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)

        btn1.setText("Button 1")
        btn2.setText("Button 2")
        btn3.setText("Button 3")

        hbox =QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn1)

        hbox.addStretch(1)
        hbox.addWidget(btn2)

        hbox.addStretch(1)
        hbox.addWidget(btn3)

        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle("addStretch 例子")


class Right(QWidget):
    def __init__(self):
        super(Right, self).__init__()

        layout = QHBoxLayout()
        layout.addStretch(0)

        layout.addWidget(QPushButton(str(1)))
        layout.addWidget(QPushButton(str(2)))
        layout.addWidget(QPushButton(str(3)))
        layout.addWidget(QPushButton(str(4)))
        layout.addWidget(QPushButton(str(5)))
        layout.addWidget(QPushButton(str(6)))

        layout.addStretch(0)

        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Right()
    win.show()
    sys.exit(app.exec_())


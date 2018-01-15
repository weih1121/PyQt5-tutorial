import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class spinDemo(QWidget):
    def __init__(self):
        super(spinDemo, self).__init__()
        self.setWindowTitle("SpinBoxDemo")
        self.resize(555, 555)

        layout = QVBoxLayout()
        self.l1 = QLabel("Current Value:")
        self.l1.setAlignment(Qt.AlignCenter)

        self.sbox = QSpinBox()
        self.sbox.setMaximum(15)
        self.sbox.setMinimum(3)

        self.sbox.valueChanged.connect(self.valueChange)

        layout.addWidget(self.l1)
        layout.addWidget(self.sbox)

        self.setLayout(layout)

    def valueChange(self):
        self.l1.setText("Current Value:" + str(self.sbox.value()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = spinDemo()
    win.show()
    sys.exit(app.exec_())
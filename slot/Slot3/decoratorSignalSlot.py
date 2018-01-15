from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class CustWidget(QWidget):
    def __init__(self):
        super(CustWidget, self).__init__()

        self.okButton = QPushButton("OK", self)
        self.okButton.setObjectName("okButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("okButton pressed!!!!")

if __name__ == '__main__':
    qpp = QApplication(sys.argv)
    win = CustWidget()
    win.show()
    sys.exit(qpp.exec_())
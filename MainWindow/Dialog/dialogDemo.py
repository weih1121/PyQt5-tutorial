import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class dialogDemo(QWidget):
    def __init__(self):
        super(dialogDemo, self).__init__()
        self.setWindowTitle("dialogDemo")
        self.resize(350, 300)

        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        btn = QPushButton("Ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = dialogDemo()
    win.show()
    sys.exit(app.exec_())
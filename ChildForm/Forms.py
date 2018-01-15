from PyQt5 import QtWidgets
from MainForm import Ui_MainForm
from ChildForm import Ui_ChildForm

from PyQt5.QtWidgets import QFileDialog

class MainForm(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.child = ChildForm()

        self.fileOpen.triggered.connect(self.openMsg)  # 菜单的点击事件是triggered
        self.fileClose.triggered.connect(self.close)
        self.actionTst.triggered.connect(self.childShow)  # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中

    def childShow(self):
        self.MainGridLayOut.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self,"打开","C:/","All Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

class ChildForm(QtWidgets.QWidget, Ui_ChildForm):
    def __init__(self):
        super(ChildForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MainForm()
    myshow.show()
    sys.exit(app.exec_())
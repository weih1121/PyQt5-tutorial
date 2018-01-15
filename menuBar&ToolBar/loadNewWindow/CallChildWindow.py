import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMainWindow
from loadNewWindow.MainWindow2 import Ui_MainWindow
from loadNewWindow.ChildWindow import Ui_Form

class MainFrom(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.setupUi(self)

        self.child = ChildrenForm()

        self.CloseFileAction.triggered.connect(self.close)
        self.CreateNewFileAction.triggered.connect(self.openMsg)
        self.AddNewWindowAction.triggered.connect(self.childShow)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "Al Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainFrom()
    win.show()
    sys.exit(app.exec_())



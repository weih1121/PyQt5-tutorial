from Group import Ui_Form, button
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


class mainForm(Ui_Form):
    def __init__(self):
        super(mainForm, self).__init__()

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainForm = mainForm()
    mainForm.show()
    sys.exit(app.exec_())
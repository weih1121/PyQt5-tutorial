import sys
from PyQt5.QtWidgets import *
from CheckBoxGroup import Ui_Form

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())
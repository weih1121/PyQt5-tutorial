from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication
from managmentLayout import Ui_MainWindow

class LayoutDemo(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(LayoutDemo, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('收益_min', self.doubleSpinBox_returns_min.text())
        print('收益_max', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min', self.doubleSpinBox_sharpmin.text())
        print('sharp比_max', self.doubleSpinBox_sharpmax.text())

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui = LayoutDemo()
    ui.show()
    sys.exit(app.exec_())
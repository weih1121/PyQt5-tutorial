import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton

class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setupUI()

    def setupUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+'

        ]

        positions = [(i, j)for i in range(5) for(j) in range(4)]
        print(positions)

        for positions, names in zip(positions, names):
            if names == '':
                continue

            btn = QPushButton(names)
            grid.addWidget(btn, *positions)

        self.move(300, 150)
        self.setWindowTitle('网络布局管理例子')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm()
    win.show()
    sys.exit(app.exec_())
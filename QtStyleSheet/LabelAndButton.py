import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class WinForm(QWidget):
    def __int__(self, parent = None):
        super(WinForm, self).__int__(parent)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['陈宏子', '秦婷婷', '折蓉蓉', '曹丽娜', '李娜',
                 '姜钰', '天霞', '王官君', '王红梅', '郭淑慧',
                 '马海娟', '孙洪山', '胡丹丹', '倪辰曦', '胡书琴',
                 '冷静', '李剑', '范志坚', '任娟娟', '何圆']

        positions = [(i, j) for i in range(4) for j in range(5)]

        for position, name in zip(positions, names):
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle("分组")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = WinForm()
    form.show()
    sys.exit(app.exec_())

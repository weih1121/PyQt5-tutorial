from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

'''
自定义信号一般流程：
    1.定义信号
    2.定义槽函数
    3.连接信号与槽函数
    4.发射信号
'''

'''
信号与槽函数的基本使用
'''
class WinForm(QWidget):
    def __init__(self):
        super(WinForm, self).__init__()
        self.setWindowTitle('内置的信号/槽示例')
        self.resize(300, 50)

        btn = QPushButton("关闭", self)
        btn.clicked.connect(self.close)


class WinForm01(QWidget):
    def __init__(self):
        super(WinForm01, self).__init__()

        btn = QPushButton("Test Button")
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(btn)

        self.setLayout(self.hlayout)

        btn.clicked.connect(self.showMsg)

    def showMsg(self):
        QMessageBox().information(self, "测试样例", "OK", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)

class QTypeSignal(QObject):
    sendMsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self):
        self.sendMsg.emit("Hello PyQt5")

class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot, self).__init__()

    def get(self, msg):
        print("QSlot get msg ->" + msg)

class QTypeSignal01(QObject):
    sendMsg = pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal01, self).__init__()

    def run(self):
        self.sendMsg.emit('The First Argument', 'The Second Arguement')

class QTypeSlot01(QObject):
    def __init__(self):
        super(QTypeSlot01, self).__init__()

    def get(self, msg1, msg2):
        print("QSlot get msg ->" + msg1 + "   " + msg2)




if __name__ == "__main__":
    send = QTypeSignal01()
    slot = QTypeSlot01()

    print('---把信号绑定到槽上---')
    send.sendMsg.connect(slot.get)
    send.run()

    print('---把信号与槽断开连接---')
    send.sendMsg.disconnect(slot.get)
    send.run()



'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WinForm01()
    win.show()
    sys.exit(app.exec_())
'''


'''
高级自定义信号与槽
'''

class CustSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(CustSignal, self).__init__()

        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int, str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6OverLoad)

        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1, "text")
        self.signal4.emit([1, 2, 3, 4])
        self.signal5.emit({"name":"zhangsan", "age":"25"})
        self.signal6[int, str].emit(1, "text")
        self.signal6[str].emit("text")

    def signalCall1(self):
        print("Signal1 emit()")

    def signalCall2(self, val):
        print("Signal2 emit, value:", val)

    def signalCall3(self, val, text):
        print("Signal3 emit, value:", val, text)

    def signalCall4(self, val):
        print("Signal4 emit, value:", val)

    def signalCall5(self, val):
        print("Signal5 emit, value:", val)

    def signalCall6(self, val, text):
        print("Signal6 emit, value:", val, text)

    def signalCall6OverLoad(self, val):
        print("SignalCall6OverLoad value:", val)

if __name__ == "__main__":
    CustSignal = CustSignal()

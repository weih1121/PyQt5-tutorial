from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys

class lineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("InputMask")

        flo = QFormLayout()
        pIPLineEdit = QLineEdit()
        pMACLineEdit = QLineEdit()
        pDateLineEdit = QLineEdit()
        pLisenceLineEdit = QLineEdit()

        pIPLineEdit.setInputMask("000.000.000.000;_")
        pMACLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_") 
        pDateLineEdit.setInputMask("0000-00-00")
        pLisenceLineEdit.setInputMask(
            ">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#"
        )

        flo.addRow("IP掩码", pIPLineEdit)
        flo.addRow("Mac掩码", pMACLineEdit)
        flo.addRow("Date掩码", pDateLineEdit)
        flo.addRow("证书掩码", pLisenceLineEdit)

        self.setLayout(flo)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec_())

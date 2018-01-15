from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)
win = QWidget()
win.setWindowTitle("Web页面中的javascript与QWebEngineView交互例子")

layout = QVBoxLayout()
win.setLayout(layout)

view = QWebEngineView()
view.setHtml('''
<html>
<head>
<title>A Demo Page</title>

<script language='javascript'>
    function completeAndReturnName() {
        var fname = document.getElementById('fname').value;
        var lname = document.getElementById('lname').value;
        var full = fname + ' ' + lname;
        
        document.getElementById('fullname').value = full;
        document.getElementById('sumit-btn').style.display = 'block';
        return full;
    }
</script>
</head>

<body>
<form>
<label for="fname">First Name:</label>
<input type="text" name="fname" id="fname"></input>
<br />
<label for="lname">Last Name:</label>
<input type="text" name="fname" id="fname"></input>
<br />
<label for="fullname">Full name:</label>
<input disabled type="text" name="fullname" id="fullname"></input>
</form>
</body>

</html>
''')

button = QPushButton('设置全名')

def js_callback(result):
    print(result)

def complete_name():
    view.page().runJavaScript('completeAndReturnName();', js_callback)

button.clicked.connect(complete_name)

layout.addWidget(view)
layout.addWidget(button)

win.show()
sys.exit(app.exec_())
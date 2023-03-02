import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Button", self)
        btn.move(10, 10)

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
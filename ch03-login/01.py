import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *

print(sys.argv)
app = QApplication(sys.argv)
ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
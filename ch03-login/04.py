import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pythoncom

app = QApplication(sys.argv)
ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")

ocx.dynamicCall("CommConnect()")
while True:
    pythoncom.PumpWaitingMessages()
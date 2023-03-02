import sys
from PyQt5.QAxContainer import *
from PyQt5.QtWidgets import *
import pythoncom

login = False
def OnEventConnect(code):
    global login 
    login = True
    print("login is done", code)

app = QApplication(sys.argv)
ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
ocx.OnEventConnect.connect(OnEventConnect)


ocx.dynamicCall("CommConnect()")
while login is False:
    pythoncom.PumpWaitingMessages()
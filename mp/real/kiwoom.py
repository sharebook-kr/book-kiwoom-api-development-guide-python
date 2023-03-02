from PyQt5.QAxContainer import *
import pythoncom 

class Kiwoom:
    def __init__(self, real_data_callback_func):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login = False

        self.ocx.OnEventConnect.connect(self.OnEventConnect)
        self.ocx.OnReceiveRealData.connect(real_data_callback_func)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while self.login is False:
            pythoncom.PumpWaitingMessages()

    def OnEventConnect(self, code):
        self.login = True   

    def SetRealReg(self, screen_no, code_list, fid_list, real_type):
        self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)", 
                              screen_no, code_list, fid_list, real_type)

    def DisConnectRealData(self, screen_no):
        self.ocx.dynamicCall("DisConnectRealData(QString)", screen_no)

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid) 
        return data
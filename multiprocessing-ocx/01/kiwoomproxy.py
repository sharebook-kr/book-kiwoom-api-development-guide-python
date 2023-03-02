import sys
from PyQt5.QtWidgets import *
from kiwoom import Kiwoom
import pythoncom

class kiwoomProxy:
    app = QApplication(sys.argv) 

    def __init__(self, method_cq, method_dq, tr_cq, tr_dq):
        self.method_cq = method_cq 
        self.method_dq = method_dq 
        self.tr_cq = tr_cq 
        self.tr_dq = tr_dq 

        self.kiwoom = Kiwoom(self.tr_dq)
        self.kiwoom.CommConnect()
        self.run()

    def run(self):
        while True:
            if not self.method_cq.empty():
                code = self.method_cq.get()
                name = self.kiwoom.GetMasterCodeName(code)
                self.method_dq.put(name)
            
            if not self.tr_cq.empty():
                code = self.tr_cq.get()
                self.kiwoom.SetInputValue("종목코드", code)
                self.kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")
            
            pythoncom.PumpWaitingMessages()

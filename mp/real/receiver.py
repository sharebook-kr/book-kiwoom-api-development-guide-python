from PyQt5.QtWidgets import *
import sys
import kiwoom


class Receiver:
    def __init__(self, queue):
        self.queue = queue
        self.app =  QApplication(sys.argv)
        self.kiwoom = kiwoom.Kiwoom(self.OnReceiveRealData)
        self.kiwoom.CommConnect()

        # real 
        self.kiwoom.SetRealReg("1000", "005930;035720", "20;10", 0)
        self.app.exec_()


    def OnReceiveRealData(self, code, real_type, data):
        if real_type == "주식체결":
            time = self.kiwoom.GetCommRealData(code, 20)
            price = self.kiwoom.GetCommRealData(code, 10)
            self.queue.put((code, time, price))



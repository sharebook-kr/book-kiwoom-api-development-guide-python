from PyQt5.QtCore import *
import kiwoom
import threading
import pythoncom

class Worker(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        name = threading.current_thread().getName()
        print(name)

        pythoncom.CoInitialize()
        self.kiwoom = kiwoom.Kiwoom()
        self.kiwoom.CommConnect()

        codes = self.kiwoom.GetCodeListByMarket(0)
        print(codes)
        pythoncom.CoUninitialize()

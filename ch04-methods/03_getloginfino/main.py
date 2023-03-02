import sys
from PyQt5.QtWidgets import *
from kiwoom import Kiwoom


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    accno = kiwoom.GetLoginInfo("ACCNO")
    accno_list = accno.split(";")[:-1]
    print(accno_list)
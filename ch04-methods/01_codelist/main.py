import sys
from PyQt5.QtWidgets import *
from kiwoom import Kiwoom


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    kospi = kiwoom.GetCodeListByMarket('0')
    for i, code in enumerate(kospi):
        print(i, code)
    print("total : ", len(kospi))
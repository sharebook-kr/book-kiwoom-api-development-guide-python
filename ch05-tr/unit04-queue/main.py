import sys
from PyQt5.QtWidgets import *
from kiwoom import Kiwoom


if __name__ == "__main__":
    app = QApplication(sys.argv)

    kiwoom = Kiwoom()
    kiwoom.CommConnect()

    kiwoom.SetInputValue("종목코드", "005930")
    kiwoom.CommRqData("myrequest", "opt10001", 0, "0101")
    tr_data = kiwoom.tr_queue.get()
    print(tr_data)
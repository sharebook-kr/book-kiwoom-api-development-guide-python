import sys
from PyQt5.QtWidgets import *
import multiprocessing as mp
from kiwoomproxy import kiwoomProxy

class MyWindow(QMainWindow):
    def __init__(self, method_cq, method_dq, tr_cq, tr_dq):
        super().__init__()
        self.method_cq = method_cq 
        self.method_dq = method_dq 
        self.tr_cq = tr_cq 
        self.tr_dq = tr_dq

        btn1 = QPushButton("method")
        btn1.clicked.connect(self.request_method)

        btn2= QPushButton("TR")
        btn2.clicked.connect(self.request_tr)

        w = QWidget()
        layout = QVBoxLayout(w)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setCentralWidget(w)

    def request_method(self):
        self.method_cq.put("005930")
        name = self.method_dq.get()
        print(name)

    def request_tr(self):
        self.tr_cq.put("005930")
        output = self.tr_dq.get()
        print(output)


if __name__ == "__main__":
    # queue 
    queues = [mp.Queue() for i in range(4)]

    # kiwoom proxy process 
    p = mp.Process(target=kiwoomProxy, args= queues, daemon=True)
    p.start()

    # UI 
    app = QApplication(sys.argv)
    win = MyWindow(*queues)
    win.show()
    app.exec_()


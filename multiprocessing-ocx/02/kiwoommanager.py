import sys
from PyQt5.QtWidgets import *
import multiprocessing as mp
from kiwoomproxy import kiwoomProxy

class KiwoomManager:
    def __init__(self):
        # method_cq, method_dq, tr_cq, tr_dq
        self.queues = [mp.Queue() for i in range(4)]

        # kiwoom proxy process 
        self.proxy = mp.Process(target=kiwoomProxy, args= self.queues, daemon=True)
        self.proxy.start()

    def put_method(self, cmd):
        self.queues[0].put(cmd)
    
    def get_method(self):
        return self.queues[1].get()

    def put_tr(self, cmd):
        self.queues[2].put(cmd)
    
    def get_tr(self):
        return self.queues[3].get()



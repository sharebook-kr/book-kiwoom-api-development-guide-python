import threading 
import time

class Worker(threading.Thread):
    def __init__(self, secs):
        super().__init__()
        print("run", threading.currentThread().getName())
        self.secs = secs

    def run(self):
        print("run", threading.currentThread().getName())
        time.sleep(self.secs)

t = Worker(5)
t.start()
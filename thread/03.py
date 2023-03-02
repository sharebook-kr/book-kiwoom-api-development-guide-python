import threading 
import time

class Worker:
    def __init__(self):
        print("__init__", threading.currentThread().getName())
        self.run()

    def run(self):
        print("run", threading.currentThread().getName())
        time.sleep(5)


t = threading.Thread(target=Worker, name="WorkerThread")
t.start()
import threading 
import time


def work():
    name = threading.current_thread().getName()
    print(f"{name} Start")
    time.sleep(5)
    print(f"{name} End")


name = threading.current_thread().getName()
print(f"{name} Start")

t1 = threading.Thread(target=work, name="SubThread")
t1.start()

name = threading.current_thread().getName()
print(f"{name} End")
    
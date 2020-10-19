# program example for multi threading
from time import sleep
from threading import *
class hellow(Thread):
    def run(self):
         for n in range(5):
            print("hema")
            sleep(3)
class hi(Thread):
    def run(self):
        for k in range(5):
            print("manu")
            sleep(3)

T1=hellow()
T2=hi()

T1.start()
sleep(3)
T2.start()

T1.join()  # to print below print code first main thread should wait other 2 threads to complte its execution then only main thread can do is task
T2.join()

print("this step get executed using main thread")
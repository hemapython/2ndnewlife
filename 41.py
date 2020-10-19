#this is the program writting after completing revision on the same
from threading import Thread
from time import sleep


class komala(Thread):
    def run(self):
        for j in range (5):
            print("hellow")
            sleep(1) # here sleep declared becoz 2 threads will print parallelly when we dont declare sleep then in 1 second itself hellow will print 5 times not sequesntially


class anu(Thread):
    def run(self):
        for i in  range(5):
            print("Hi")
            sleep(1)


t1=komala()
t2=anu()

print(t1.start())# by the time u call "start()" the program start to cal thread in the program when run() being initiated
sleep(0.3)
print(t2.start()) # now t1 and t2 threads created

print(t1.is_alive())
print(t2.getName())

t1.join() # just join() enable program to wait for the thread to get terminate in the program
t2.join()


print("bye") # here bye is printing before completing the 2 thread output in between itself its printing hence we should declare join() method





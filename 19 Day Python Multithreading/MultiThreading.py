from threading import Thread  
import time # import time module 

class data1(Thread):
  def run(self):
    for i in range(10):
      print(i,'----thread 1--------')
      time.sleep(1)

class data2(Thread):
  def run(self):
    for i in range(10):
      print(i,'*****Thread 2*********')
      time.sleep(2)

obj0 = data1()
obj1 = data2()
obj0.start()
obj1.start()      
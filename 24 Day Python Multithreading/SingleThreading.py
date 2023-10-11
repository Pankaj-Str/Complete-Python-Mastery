from threading import Thread  
import time # import time module 

class threading1():
  def run():
    for i in range(10):
      print('Welcome Thread 1 ---- ',i)
      time.sleep(1)

obj = threading1
obj.run()
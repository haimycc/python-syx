import threading
import time,random

class GCounter(object):
    def __init__(self):
        self.lock=threading.Lock()
        self.value=0

    def increment(self):
        self.lock.acquire()
        self.value=self.value+1
        self.lock.release()

#定义全局变量对象
g_counter=GCounter()

#定义线程类
class ThreadWroker(threading.Thread):
    def run(self):
        for i in range(10):
            value=g_counter.increment()
            time.sleep(random.randint(10,100)/1000)
            print(self.getName()+"--task"+str(i)+" finished,value is "+str(g_counter.value))

#创建线程类对象
for i in range(10):
    ThreadWroker().start()


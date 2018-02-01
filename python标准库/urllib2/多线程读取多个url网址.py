#!/usr/bin/evn python

import queue
import threading
import urllib
import time


#网址
hosts=["http://www.baidu.com","http://www.qq.com",
       "http://www.sina.com","http://www.126.com",
       "http://www.163.com"]

#通过继承方式来创建线程
class ThreadUrl(threading.Thread):
    """this is thread for url"""
    def __int__(self,arg):
        threading.Thread.__init__(self)
        self.queue=arg

    def run(self):
        while True:
            host=self.queue.get()
            url=urllib.urlopen(host)
            print(url.read(1024))
            self.queue.task_done()





#创建队列
q=queue.Queue()

#开始事件
start=time.time()

def Test():
    #开启5个线程
    for i in range(5):
        t=ThreadUrl(q)
        t.setDaemon(True)
        t.start()
    for host in hosts:
        q.put(host)
    q.join()

Test()
print("Elapsed Time: %s" % (time.time() - start))
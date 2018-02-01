# -*- coding:utf-8 -*-
import threading
import datetime

#通过派生子类来运行线程
class ThreadClass(threading.Thread):
    def run(self):
        now=datetime.datetime.now()
        print("%s says hello world at time:%s" % (self.getName(),now))


for i in range(2):
    t=ThreadClass()
    t.start()





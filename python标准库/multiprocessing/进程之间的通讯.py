#-*- coding:UTF-8 -*-
from multiprocessing import Process,Queue
import os,time,random

#写进程,接受一个Queue作为参数
def write(q):
    print("Process to write:%s" % os.getpid())
    for value in ["A","B","C"]:
        print("Put %s to queue" % value)
        #往Queue发送消息
        q.put(value)
        time.sleep(random.random())

#读进程,接受一个Queue作为参数
def read(q):
    print("Process to read:%s" % os.getpid())
    #死循环，不断读取消息
    while True:
        value=q.get(True)
        print("Get %s from queue" % value)

#创建Queue对象和进程对象
queue=Queue()
pw=Process(target=write,args=(queue,))
pr=Process(target=read,args=(queue,))
#开启进程
pw.start()
#开启读进程
time.sleep(5)
pr.start()
#等待进程借宿
pw.join()
#pr.join()
time.sleep(5)
pr.terminate()
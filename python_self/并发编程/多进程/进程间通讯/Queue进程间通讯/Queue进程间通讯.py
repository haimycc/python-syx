# -*- coding:utf-8 -*-
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    #给写进程传递queue对象
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        #写进程网queue对象写数据
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    #给读进程传递queue对象
    print('Process to read: %s' % os.getpid())
    while True:
        #读进程从queue对象读数据
        value = q.get(True)
        print('Get %s from queue.' % value)



if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    #创建父子进程通讯的queue对象
    q = Queue()
    #创建2个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

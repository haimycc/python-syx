# -*- coding:utf-8 -*-
from multiprocessing import Pool
import os, time, random

#子进程的任务
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    #主进程的pid
    print('Parent process %s.' % os.getpid())
    #开启具有4个进程的进程池
    p = Pool(4)
    #开启子进程
    for i in range(5):
        #因为进程池同时只可以有4个进程同时再跑，所以第五个进程只可以等到有空闲进程的时候才跑
        p.apply_async(long_time_task, args=(i,))
    #等待
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

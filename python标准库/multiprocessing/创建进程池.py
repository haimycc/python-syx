#-*-coding:UTF-8 -*-
from multiprocessing import Pool
import os,time,random

#交给线程池的任务
#交给线程池的任务task1，task2
def long_time_task(name):
    print("Run task %s (%s)..." % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print("task %s run %02.f seconds" %s (name,(end-start)))


if __name__=="__main__":
    print("main process %s." % os.getpid())
    #创建线程池
    p=Pool(4)
    for i in range(10):
        #为线程池分配10个任务，这么一来，并发度只有4个
        p.apply_async(long_time_task,args=(i,))
    print("main process is waitting all subprocess done...")
    p.close()
    p.join()
    print("all subprocess is done")
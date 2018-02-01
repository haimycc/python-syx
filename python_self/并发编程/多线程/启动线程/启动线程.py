# -*- coding:utf-8 -*-
import time, threading

# 新线程执行的代码:
def loop():
    #线程开启
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        #n递增
        n = n + 1
        #线程名和n
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    #线程退出
    print('thread %s ended.' % threading.current_thread().name)


#主线程启动
print('thread %s is running...' % threading.current_thread().name)
#threading模块启动线程，线程函数式loop，线程参数是LoopThread作为线程名
t = threading.Thread(target=loop, name='LoopThread')
#开启线程
t.start()
#线程等待主线程
t.join()
#主线程退出
print('thread %s ended.' % threading.current_thread().name)

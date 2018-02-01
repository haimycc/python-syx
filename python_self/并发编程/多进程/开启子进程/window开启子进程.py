# -*- coding:utf-8 -*-
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    #父进程
    print('Parent process %s.' % os.getpid())
    #开启子进程，传递子进程的参数
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    #开启子进程
    p.start()
    #等待子进程关闭
    p.join()
    print('Child process end.')


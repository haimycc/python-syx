from multiprocessing import Process
import os

#子进程做什么事情
def run_proc(name):
    print("Run child process %s (%s)..." % (name,os.getpid()))

if __name__=="__main__" :
    print("parent process %s." % (os.getpid()))
    #创建子进程
    p=Process(target=run_proc,args=("test",))
    #开启子进程
    p.start()
    #关闭子进程
    p.join()
    print("child process end.")


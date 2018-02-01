import time,threading

#线程要执行的函数
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n=0
    while n<5 :
        n=n+1
        print("thread %s >>> %s" % (threading.current_thread().name,n))
        time.sleep(1)
    print("thread %s is ending..." % threading.current_thread().name)

#创建线程对象
t_obj=threading.Thread(target=loop,name="Loopthread")
#开启线程
t_obj.start()
#等待线程join
t_obj.join()
print("Main thread is ending...")
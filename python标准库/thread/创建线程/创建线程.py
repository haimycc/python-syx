import thread
import time,random

#这个线程worker
def worker():
    for i in range(50):
        time.sleep(random.randint(10,100)/1000)
        print(thread.get_ident()+"--task "+i+" finished")

#开2个worker线程
for i in range(2):
    #开启线程
    thread.start_new_thread(worker,())

time.sleep(10)
print("goodbye")
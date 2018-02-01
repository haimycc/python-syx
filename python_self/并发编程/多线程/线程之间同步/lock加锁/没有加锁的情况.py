# -*- coding:utf-8 -*-
import time, threading

# 假定这是你的银行存款:
# 这是一个全局变量
balance = 0

#线程的过程，不断读写全局变量
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

#线程过程
def run_thread(n):
    for i in range(100000):
        change_it(n)

#线程t1,t2开启,然后传递参数。
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

#开启2个线程
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

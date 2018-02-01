# -*- coding:utf-8 -*-
def generateFunction():
    list=["zxp","lqh","zll"]
    for element in list:
        print(element)
        #跑到yield就不会再跑了，一直等到下一个next函数被调用才会继续从yield继续跑起来
        yield element

f=generateFunction()
f.__next__()
f.__next__()
f.__next__()

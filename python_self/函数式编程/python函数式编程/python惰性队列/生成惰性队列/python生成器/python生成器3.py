# -*- coding:utf-8 -*-
def generateFunction():
    #yield惰性队列收到控制逻辑控制
    while True:
        yield 1
    return None

f=generateFunction()
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())



def generateFunction():
    #yield惰性队列收到控制逻辑控制
    if True:
        yield 1
    else:
        yield 2
    return None
f=generateFunction()
print(f.__next__())
#抛出StopIteration
print(f.__next__())
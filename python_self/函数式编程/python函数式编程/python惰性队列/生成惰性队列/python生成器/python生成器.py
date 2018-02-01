# -*- coding:utf-8 -*-
def generateFunction():
    yield 1
    yield 2
    yield 3
    yield 4
    return None

#f是生成器对象
f=generateFunction()
print(f)
#每次调用生成器，就会生成一个元素
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

#StopIteration，如果生成器借宿，那么就会抛出异常
#print(f.__next__())






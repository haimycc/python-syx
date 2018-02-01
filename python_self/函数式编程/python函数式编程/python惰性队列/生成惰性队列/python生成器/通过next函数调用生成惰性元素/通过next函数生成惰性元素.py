# -*- coding:utf-8 -*-
def function():
    for i in range(10):
        #生成惰性元素
        yield i

f=function()
#next函数调用function生成惰性元素
print(next(f))
print(next(f))
print(next(f))
print(next(f))




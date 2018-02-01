# -*- coding:utf-8 -*-
#装饰器函数
def BeforeFunction(func):
    #定义一个装饰器函数
    def InnerFunction(*args,**kw):
        #装饰器函数做一些额外操作
        print("before function")
        func(*args,**kw)
        print("after function")
        return
    return InnerFunction


@BeforeFunction
def Hello():
    print("hello,world")

#BeforeFunction(Hello)

Hello()
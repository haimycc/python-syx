# -*- coding:utf-8 -*-

#表示arg是一个tuple,接受tuple对象或者list对象作为参数
def fun(arg1,arg2,*args):
    print("arg1 is ",arg1)
    print("arg2 is ",arg2)
    for arg in args:
        print("arg is ",arg)
    return

#元组参数只可以做位置参数
fun(1,2,*[3,4,5,6,7,8,9,10])

#元组参数只可以做位置参数
fun(*[1,2,3,4,5,6,7,8,9,10])
# -*- coding:utf-8 -*-

#表示arg是一个tuple,接受tuple对象或者list对象作为参数
def function(*args):
    for arg in args:
        print(arg)
    return

list=["zxp","love","zll"]
function(*list)
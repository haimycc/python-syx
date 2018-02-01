# -*- coding:utf-8 -*-
#全局变量初始化
num=0
#全局遍历被覆盖
num=1
print(num)
#全局遍历被覆盖
def num(arg1,arg2):
    return arg1,arg2
print(num)
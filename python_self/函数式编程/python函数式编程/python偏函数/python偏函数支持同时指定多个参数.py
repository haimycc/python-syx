# -*- coding:utf-8 -*-
from functools import partial

#定义函数，具有5个参数的函数
def function(arg1,arg2,arg3,arg4,arg5):
    return arg1+arg2+arg3+arg4+arg5
#偏函数支持同时指定多个值
function5to5=partial(function,1,2,3,4,5)
#偏函数调用
print(function5to5)
print(function5to5())
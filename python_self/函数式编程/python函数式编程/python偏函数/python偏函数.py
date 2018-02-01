# -*- coding:utf-8 -*-
from functools import partial

#定义函数，具有5个参数的函数
def function(arg1,arg2,arg3,arg4,arg5):
    return arg1+arg2+arg3+arg4+arg5

#定义偏函数
function1to5=partial(function,1)
function2to5=partial(function1to5,2)
function3to5=partial(function2to5,3)
function4to5=partial(function3to5,4)
function5to5=partial(function4to5,5)

#函数调用
print(function5to5)
print(function5to5())

# -*- coding:utf-8 -*-
from functools import partial

def function(arg1=0,arg2=0,arg3=0):
    return arg1+arg2+arg3

f1=partial(function,arg2=1)
#f1=function(0,1,0)
print(f1())

#f2=function(1,1,0)
f2=partial(f1,arg1=1)
print(f2())

#f3=function(1,1,1)
f3=partial(f2,arg3=1)
print(f3())

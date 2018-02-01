# -*- coding:utf-8 -*-

def function(arg1,arg2,name,age):
    print(arg1)
    print(arg2)
    print(name)
    print(age)
    return

#必须先搞定位置参数后，再考虑关键字参数
function(1,2,age=4,name=3)
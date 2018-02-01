# -*- coding:utf-8 -*-
def OuterFunction():
    #自由变量时list列表
    dict=[0,1,2,3,4,5]
    def Inner():
        print(dict)
    return Inner

f=OuterFunction()
f()
f()
f()
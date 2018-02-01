# -*- coding:utf-8 -*-
def cloFunction():
    num=[0]
    #闭包
    def function():
        print("count is ",num[0])
        num[0]+=1
        #上面的闭包共享外部函数的列表，所以这里要注意，如果是普通的基本变量，那么是无法共享的。
        #个人猜测必须是复合数据类型
    return function

f=cloFunction()
f()
f()
f()


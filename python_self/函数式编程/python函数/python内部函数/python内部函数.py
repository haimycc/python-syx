# -*- coding:utf-8 -*-

def function(arg1,arg2):
    def Add(arg1,arg2):
        return arg1+arg2
    def Del(arg1,arg2):
        return arg1-arg2
    def Mul(arg1,arg2):
        return arg1*arg2
    def Div(arg1,arg2):
        return arg1/arg2
    print(Add(arg1,arg2))
    print(Del(arg1,arg2))
    print(Mul(arg1,arg2))
    print(Div(arg1,arg2))

function(1,1)
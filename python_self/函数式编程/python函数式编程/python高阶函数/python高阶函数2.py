# -*- coding:utf-8 -*-
def my_add(arg1,arg2):
    return arg1+arg2

def my_del(arg1,arg2):
    return arg1-arg2

def my_mul(arg1,arg2):
    return arg1*arg2

def my_div(arg1,arg2):
    return arg1/arg2

#高阶函数
def function(f,arg1,arg2):
    return f(arg1,arg2)

print(function(my_add,1,1))
print(function(my_del,1,1))
print(function(my_mul,1,1))
print(function(my_div,1,1))
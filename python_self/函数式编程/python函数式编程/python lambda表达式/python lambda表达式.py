# -*- coding:utf-8 -*-
#lambda匿名函数
my_add=lambda x,y: x+y
my_del=lambda x,y: x-y
my_mul=lambda x,y: x*y
my_div=lambda x,y: x/y

#高阶函数
def function(f,arg1,arg2):
    return f(arg1,arg2)

print(function(my_add,1,1))
print(function(my_del,1,1))
print(function(my_mul,1,1))
print(function(my_div,1,1))


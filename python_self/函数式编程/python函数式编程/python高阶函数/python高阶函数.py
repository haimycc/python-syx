# -*- coding:utf-8 -*-
#高阶函数，因为python是动态类型语言，
#没有指定参数的类型，所以非常适合做高阶函数
def function(f,arg1,arg2):
    return f(arg1,arg2)

print(function(lambda x,y:x+y,1,1))
print(function(lambda x,y:x-y,1,1))
print(function(lambda x,y:x*y,1,1))
print(function(lambda x,y:x/y,1,1))




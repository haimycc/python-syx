# -*- coding:utf-8 -*-


#这是一个函数
#因为python是动态类型，所以支持类型推导
#所以这个函数可以接受不同类型的参数
def function(type_arg):
    print(type_arg)

function(1)
function(1.0)
function(100000000000000000000000000000)
function(lambda x:x)
function(True)
function(False)
function(None)
function("hello,world")
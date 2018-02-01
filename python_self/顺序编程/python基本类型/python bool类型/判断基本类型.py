# -*- coding:utf-8 -*-
import builtins

#判断整数类型
print(type(30) is builtins.int)
#字符串
print(type("hello,world") is builtins.str)
#list
print(type([1,2,3]) is builtins.list)
#tuple
print(type((1,2,3)) is builtins.tuple)
#这个不是slice类型
print(type([1,2,3,4,5,6,7][:]) is builtins.slice)
print(type((1,2,3)[:]) is builtins.slice)
print(type([1,2,3,4][1:2]) is builtins.slice)
#list
print(type([1,2,3,4,5,6,7][:]) is builtins.list)
#dict
print(type({"name":"zxp","age":30}) is builtins.dict)



# -*- coding:utf-8 -*-
def function():
    return True

#重载成员函数失败，因为python是动态语言
#python具有命名空间的区别
#python不允许在同一个命名空间中有多个相同的名字
def function(arg):
    return False

print(function())
print(function(1))

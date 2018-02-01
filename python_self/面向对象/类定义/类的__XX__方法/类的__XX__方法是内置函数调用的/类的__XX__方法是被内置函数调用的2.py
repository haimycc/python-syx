# -*- coding:utf-8 -*-
class Person(object):
    #__str__方法其实就是给str函数调用的
    def __str__(self):
        return "hello,world"


obj=Person()
print(obj)
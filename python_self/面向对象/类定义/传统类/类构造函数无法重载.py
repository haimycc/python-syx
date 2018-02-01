# -*- coding:utf-8 -*-
class Person:
    #定义类构造函数
    def __init__(self):
        self.name="zxp"
        self.age=30
    #如果再定义一个构造函数，那么这个构造函数就是重定义前面的构造函数
    #def __init__(self,name,age):
    #    self.name=name
    #    self.age=age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age

obj1=Person()
print(obj1.GetName())
print(obj1.GetAge())

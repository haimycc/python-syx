# -*- coding:utf-8 -*-
#传统类定义
class Person:
    #类构造函数
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #类成员函数
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age


obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())
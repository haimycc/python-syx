# -*- coding:utf-8 -*-
class Person:
    #构造函数采用默认的参数
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age

#构造函数采用默认参数
obj=Person()
print(obj.GetName())
print(obj.GetAge())
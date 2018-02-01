# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age

obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())
# -*- coding:utf-8 -*-
class Person:
    #和self无关的，都是类型的静态数据
    name="default"
    age=0
    def __init__(self,name,age):
        #和类对象有关的，都是类型对象相关的非静态数据
        self.name=name
        self.age=age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age


obj=Person("zxp",30)
#获取类型的成员
print(Person.name)
print(Person.age)

#获取类实例对象成员
print(obj.name)
print(obj.age)
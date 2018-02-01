# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #str函数可以获取python类实例对象的str表达式
    def __str__(self):
        return "person name is "+self.name+",person age is "+str(self.age)


obj=Person("zxp",30)
#通过print，调用Person类型的str函数，把python实例对象字符串化
print(obj)
#通过str，获取python类实例对象的字符串化
print(str(obj))
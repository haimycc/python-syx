# -*- coding:utf-8 -*-
import  builtins

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __cmp__(self, other):
        if self.name!=other.name:
            return cmp(self.name,other.name)
        else:
            return cmp(self.age,other.age)


obj1=Person("zxp",30)
obj2=Person("lqh",30)

print(cmp(obj1,obj2))

# -*- coding:utf-8 -*-
class Person(object):
    name="defalut"
    age=0
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

obj=Person()
print(obj.getName())
print(obj.getAge())
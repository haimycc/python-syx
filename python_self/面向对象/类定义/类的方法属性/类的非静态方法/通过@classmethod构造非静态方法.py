# -*- coding:utf-8 -*-
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def ClassMethod(self):
        print("this is ClassMethod")

obj=Person("zxp",30)
obj2=Person("lqh",30)
obj.ClassMethod()
obj2.ClassMethod()
# -*- coding:utf-8 -*-
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def SayHello(self):
        print("hello,",self.name)

    SayHello=classmethod(SayHello)

obj=Person("zxp",30)
obj.SayHello()

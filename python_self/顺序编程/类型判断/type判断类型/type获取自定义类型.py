# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#判断自定义类型的类型
print(type(Person("zxp",30)))
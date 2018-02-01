# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Man(Person):
    #如果没有定义__init__函数，那么就继承基类的__init__函数
    def __init__(self,name,age):
        super().__init__(name,age)

obj=Person("zxp",30)
print(isinstance(obj,Person))
print(isinstance(obj,object))
print(isinstance(obj,Man))

man=Man("zxp",30)
print(isinstance(man,Person))
print(isinstance(man,object))
print(isinstance(man,Man))
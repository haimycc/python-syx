# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

#obj1和obj2指向相同的内存块
obj1=Person("zxp",30)
obj2=obj1
#obj3指向不同的内存块，虽然内存相同
obj3=Person("zxp",30)


print(id(obj1))
print(id(obj2))
print(id(obj3))
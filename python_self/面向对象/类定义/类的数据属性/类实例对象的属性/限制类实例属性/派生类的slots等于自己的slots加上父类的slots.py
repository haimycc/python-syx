# -*- coding:utf-8 -*-
class Person(object):
    #限制了Person类实例对象的属性
    __slots__=("name","age")
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Man(Person):
    #派生类实例对象的属性=父类的实例对象slots+派生类的实例对象的slots
    __slots__ = ("address")
    def __init__(self,name,age,address):
        super().__init__(name,age)
        self.address=address


obj=Person("zxp",30)
obj2=Man("zxp",30,"深圳市区")

print(obj2.name)
print(obj2.age)
print(obj2.address)

#错误，这个属性没有在slots中
obj2.other="other"

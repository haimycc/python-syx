# -*- coding:utf-8 -*-
class Person(object):
    #__slots__属性用来限制python类型实例对象的属性
    __slots__=("name","age")
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=Person("zxp",30)
#因为address这个属性不存在slots中，所以无法创建
obj.address="深圳市区"


# -*- coding:utf-8 -*-
class Person(object):
    name="zxp"
    age=30

#动态增加类型的静态数据成员
Person.address="广东省汕头市"


obj=Person()
print(obj.name)
print(obj.age)
print(obj.address)
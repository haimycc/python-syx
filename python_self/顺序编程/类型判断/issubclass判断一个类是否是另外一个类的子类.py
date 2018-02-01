# -*- coding:utf-8 -*-
class Person:
    pass

#如果是相同类型
if issubclass(Person,Person):
    print("Person is subclass of Person")
else:
    pass

#Person是object的子类
if issubclass(Person,object):
    print("Person is subclass of object")
else:
    pass

#Person是int的子类
if issubclass(Person,int):
    print("Person is subclass of int")
else:
    pass
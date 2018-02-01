# -*- coding:utf-8 -*-

class Person(object):
    pass


obj1=Person()
obj2=Person()
obj3=Person()

tuples=(obj1,obj2,obj3)
if obj1 in tuples:
    print("obj1 in tuples")
if obj2 in tuples:
    print("obj2 in tuples")
if obj3 in tuples:
    print("obj3 in tuples")
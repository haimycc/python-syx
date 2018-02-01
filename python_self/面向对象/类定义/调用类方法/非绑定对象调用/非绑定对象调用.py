# -*- coding:utf-8 -*-
class Person(object):
    def f1(self):
        print("this is Person::f1()")
    def f2(self):
        print("this is Person::f2()")

obj=Person()
#非绑定对象调用就是通过直接调用类方法，然后把类实例对象传入
Person.f1(obj)
Person.f2(obj)
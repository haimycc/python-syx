# -*- coding:utf-8 -*-
class Father(object):
    def f1(self):
        print("this is Father::f1()")
    def f2(self):
        print("this is Father::f2()")

class Son(Father):
    def f3(self):
        print("this is Son::f3()")

obj=Son()
obj.f1()
obj.f2()
obj.f3()
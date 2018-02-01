# -*- coding:utf-8 -*-
class Person(object):
    def f1(self):
        print("this is Person::f1()")
    def f2(self):
        print("this is Person::f2()")

class Student(Person):
    def f3(self):
        print("this is Student::f3()")

obj=Student()
obj.f1()
obj.f2()
obj.f3()
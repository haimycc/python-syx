# -*- coding:utf-8 -*-
class Person(object):
    pass

class Student(Person):
    pass

class Man(Person):
    pass

class Woman(Person):
    pass

#python列表支持不同的python自定义类型
list=[Person(),Student(),Man(),Woman()]
print(list)
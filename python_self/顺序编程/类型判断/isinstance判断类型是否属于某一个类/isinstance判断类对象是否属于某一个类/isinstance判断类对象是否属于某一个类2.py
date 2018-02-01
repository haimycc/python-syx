# -*- coding:utf-8 -*-
class Person(object):
    pass

class Student(Person):
    pass

#类对象
obj=Student()
#判断类对象是否是父类
print(isinstance(obj,Person))
print(isinstance(obj,Student))


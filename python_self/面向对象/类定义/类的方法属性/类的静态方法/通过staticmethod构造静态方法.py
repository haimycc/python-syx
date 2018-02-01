# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 声明这个方法为静态方法，也就是不需要self对象传入
    def StaticMethod():
        print("this is StaticMethod")

    StaticMethod = staticmethod(StaticMethod)


obj = Person("zxp", 30)
obj.StaticMethod()

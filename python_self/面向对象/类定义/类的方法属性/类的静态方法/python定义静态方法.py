# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 如果是这种方法，那么编译时会出错，提示需要传递self
    def StaticMethod():
        print("this is StaticMethod")


obj = Person("zxp", 30)
obj.StaticMethod()

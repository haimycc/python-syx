# -*- coding:utf-8 -*-
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 声明这个方法为静态方法，也就是不需要self对象传入
    # 如果没有@staticmethod，那么调用StaticMethod就会要求传入self对象
    @staticmethod
    def StaticMethod():
        print("this is StaticMethod")


obj = Person("zxp", 30)
obj2 = Person("lqh", 30)

print(obj.name)
print(obj.age)
print(obj2.name)
print(obj2.age)

obj.StaticMethod()
obj2.StaticMethod()

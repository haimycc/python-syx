# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #自定义__getattr__,要是类实例对象找不到这个属性，就会调用这个函数
    def __getattr__(self, item):
        if item == "say_hello" :
            def function():
                print("hello,",self.name)
            return function


obj=Person("zxp",30)
f=obj.say_hello
f()
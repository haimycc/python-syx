# -*- coding:utf-8 -*-
class MyClass:
    #静态数据类型
    num=0
    def __init__(self):
        #非静态数据类型
        self.foo=100

obj=MyClass()
print(getattr(obj,"num"))
print(getattr(obj,"foo"))
#从名字空间删除这个名字
delattr(obj,"foo")
print(hasattr(obj,"foo"))

#从类型的名字空间中删除这个名字
delattr(MyClass,"num")
print(hasattr(obj,"num"))

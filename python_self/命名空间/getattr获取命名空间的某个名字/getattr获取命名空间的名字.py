# -*- coding:utf-8 -*-
class MyClass:
    #静态数据类型
    num=0
    def __init__(self):
        #非静态数据类型
        self.foo=100


obj=MyClass()
#获取静态数据成员
print(getattr(obj,"num"))
#获取非静态数据成员
print(getattr(obj,"foo"))
#获取静态数据成员
print(getattr(MyClass,"num"))
#这个是获取不到的，因为这个是类实例的数据成员
#print(getattr(MyClass,foo))
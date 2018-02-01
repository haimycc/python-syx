# -*- coding:utf-8 -*-
class Person:
    pass
#创建类实例对象
obj=Person()
#类实例对象是否属于某一个类型
if isinstance(obj,Person) :
    print("obj is instance of Person")
else:
    print("obj is not instance of Person")

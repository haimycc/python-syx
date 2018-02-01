# -*- coding:utf-8 -*-
if type(10) is int:
    print("type(10) is int")
else:
    print("type(10) is not int")



class Person:
    pass

#type计算类实力对象，判断是不是Person类型
obj=Person()
if type(obj) is Person :
    print("type(obj) is Person")
else:
    print("type(obj) is not Person")


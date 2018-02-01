#!/bin/env python

#通过python脚本形式来执行python程序，只需要给py脚本加上可执行权限就可以了

#Person类
class Person(object):
        def __init__(self,arg_name,arg_age):
                self.name=arg_name
                self.age=arg_age
        def GetName(self):
                return self.name

        def GetAge(self):
                return self.age

obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())

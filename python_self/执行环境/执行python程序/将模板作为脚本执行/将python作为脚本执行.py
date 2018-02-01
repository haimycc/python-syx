#!/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

#通过这种方式执行,那么就会自动调用python解释器，把python脚本作为类似shell脚本的方式执行

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

with open("/etc/passwd","a+") as f:
    for line in f.readlines():
        print(line)

sys.exit()
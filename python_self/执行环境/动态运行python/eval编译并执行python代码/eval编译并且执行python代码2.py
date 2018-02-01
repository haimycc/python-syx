# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,arg_nama,arg_age):
        self.name=arg_nama
        self.age=arg_age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age


exec("""
obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())
""")

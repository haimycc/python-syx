# -*- coding:utf-8 -*-
class Person:
    def __init__(self,arg):
        self.container=arg
    def __getattr__(self, item):
        return getattr(self.container,item)
    def __str__(self):
        return str(self.container)


obj=Person([])
#list的append方法
obj.append(1)
obj.append(2)
print(obj)
#list的count方法
print(obj.count(1))
#list的reverse方法
obj.reverse()
print(obj)
#list的sort方法
obj.sort()
print(obj)

obj=Person({})
obj=obj.fromkeys(("name","age","addr"),("zxp",30,"广东省深圳市"))
print(obj)



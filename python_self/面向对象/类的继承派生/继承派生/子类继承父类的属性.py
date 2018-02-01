# -*- coding:utf-8 -*-
class Father(object):
    name="周晓鹏"
    age=30

class Son(Father):
    address="广东省深圳市区"


#子类调用父类的属性
obj=Son()
print(obj.name)
print(obj.age)
print(obj.address)
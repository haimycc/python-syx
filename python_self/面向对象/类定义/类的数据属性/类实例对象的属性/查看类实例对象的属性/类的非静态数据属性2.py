# -*- coding:utf-8 -*-
class Person:
    def __init__(self,arg_name,arg_age):
        self.name=arg_name
        self.age=arg_age


#获取类实例对象
obj=Person("zxp",30)
#获取类实例对象的map字典
print(dir(obj))
#获取类实例对象自己的map字典,具有name和age
print(obj.__dict__)
#Person类型自己的map字典没有name和age字段
print(Person.__dict__)


#更新类实例对象
obj.addr="中国"
print(obj.__dict__)
print(Person.__dict__)

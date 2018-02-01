# -*- coding:utf-8 -*-
class Person:
    #类型的静态数据属性
    name="defalut"
    age=0
    addr="中国"

obj=Person()
print(obj.name)
print(obj.age)
print(obj.addr)
#获取类型实例的dict字典
print(dir(obj))
#类实例对象自己的dict字典为空{}
print(obj.__dict__)
#获取类型的dict字典, 静态数据成员都在Person的命名空间中
print(Person.__dict__)






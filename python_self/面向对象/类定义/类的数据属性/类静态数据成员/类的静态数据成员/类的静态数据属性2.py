# -*- coding:utf-8 -*-
class Person(object):
    version=1.0
#获取类实例对象
obj=Person()
#搜索类型的数据成员
print(Person.version)
#搜索类实例对象的数据成员,
print(obj.version)

#修改类型的数据成员
Person.version+=1.1
print(Person.version)
print(obj.version)



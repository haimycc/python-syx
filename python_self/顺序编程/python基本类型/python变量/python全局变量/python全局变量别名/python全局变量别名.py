# -*- coding:utf-8 -*-
num1=100
num2=num1
print(id(num1))
print(id(num2))


list1=[1,2,3]
list2=list1
print(id(list1))
print(id(list2))

tuple1=(1,2,3)
tuple2=tuple1
print(id(tuple1))
print(id(tuple2))

map1={"name":"zxp","age":30}
map2=map1
print(id(map1))
print(id(map2))


class Person:
    pass

obj1=Person()
obj2=obj1
print(id(obj1))
print(id(obj2))

# -*- coding:utf-8 -*-
class Person:
    #类型的静态数据成员
    container={"name":"default","age":0}

obj=Person()
#虽然修改了,不过修改的是类型的静态数据成员
obj.container["name"]="zxp"
obj.container["age"]=30
obj2=Person()
#虽然修改了，不过修改的是类型的静态数据成员
obj2.container["addr"]= "广东省深圳市"

print(obj.__dict__)
print(obj2.__dict__)
print(Person.__dict__)
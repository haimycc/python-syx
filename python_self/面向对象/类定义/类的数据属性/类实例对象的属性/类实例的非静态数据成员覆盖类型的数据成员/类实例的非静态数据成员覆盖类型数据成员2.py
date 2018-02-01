# -*- coding:utf-8 -*-
class Person:
    name="default"
    age=0
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age


#先找类实例对象的属性，再找类型的属性
obj=Person()
print(obj.name)
print(obj.age)
obj2=Person()
print(obj2.name)
print(obj2.age)

#先找类型实例对象的属性，再找类型的属性
obj3=Person()
obj3.name="zxp"
obj3.age=30
#删除类实例对象的属性
del obj3.name
del obj3.age
print(obj3.name)
print(obj3.age)



#name和age都是类型的数据属性，而不是类实例对象的数据属性
print(obj.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)







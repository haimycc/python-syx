# -*- coding:utf-8 -*-
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __repr__(self):
        return "Person(" + "\""+self.name+"\","+str(self.age)+")"


#对python类类型对象进行repr，把python字符串对象进行python代码化
obj=Person("zxp",30)
#把python类型对象给字符串化为python代码
#3.5不再支持``反双引号
repr_obj=`obj`
print(repr_obj)
#把python代码再进行求值为python内存对象
obj=eval(repr_obj)
print(obj.name)
print(obj.age)


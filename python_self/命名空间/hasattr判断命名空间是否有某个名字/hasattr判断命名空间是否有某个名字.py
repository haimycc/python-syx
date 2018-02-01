# -*- coding:utf-8 -*-
class MyClass:
    #静态数据类型
    num=0
    def __init__(self):
        #非静态数据类型
        self.foo=100

#hasattr判断类实例对象是否有这个attr
myInst=MyClass()
if hasattr(myInst,"foo") :
    print("myInst has attr:foo")
else:
    print("myInst hasn't attr:foo")

#判断类实例是否有这个attr
#这里是先查类实力，再查类型
if hasattr(myInst,"num"):
    print("myInst has attr:num")
else:
    print("myInst hasn't attr:num")

#判断类型是否有这个attr
if hasattr(MyClass,"num"):
    print("MyClass has attr:num")
else:
    print("MyClass hasn't attr:num")

#判断类型是否有这个attr
#这里foo是实例对象的名字，所以找不到
if hasattr(MyClass,"foo"):
    print("MyClass has attr:num")
else:
    print("MyClass hasn't attr:foo")
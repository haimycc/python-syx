# -*- coding:utf-8 -*-
class MyClass:
    #静态数据类型
    num=0
    def __init__(self):
        #非静态数据类型
        self.foo=100

#获取类实例对象
obj=MyClass()
#给类实例对象增加名字
setattr(obj,"name","zxp")
setattr(obj,"age",30)
print(obj.__dict__)
print(MyClass.__dict__)


#给类型增加静态类型成员
setattr(MyClass,"zxp-name","zxp")
setattr(MyClass,"zxp-age",30)
print(MyClass.__dict__)


#判断类实力对象是否可以找到类型的名字
if hasattr(obj,"zxp-name") :
    print(getattr(obj,"zxp-name"))

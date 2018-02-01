# -*- coding:utf-8 -*-
def function():
    "this is my function"
    return True

obj=function
print(obj.__doc__)
#修改函数属性
obj.__doc__="this is not my function"
obj.__version__="1.0"
#获取函数属性
print(obj.__doc__)
print(obj.__version__)
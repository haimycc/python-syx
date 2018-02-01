# -*- coding:utf-8 -*-
import types

def fn():
    pass
#通过types模块来判断type对象的类型
print(type(fn)==types.FunctionType)
print(type(lambda x:x)==types.LambdaType)
print((x for x in range(10))==types.GeneratorType)
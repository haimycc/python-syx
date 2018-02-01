# -*- coding:utf-8 -*-
#判断基本类型
print(isinstance(123,int))
print(isinstance("a",str))
print(isinstance(b"a",bytes))

#判断某一个类型的对象是否属于某一种类型
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

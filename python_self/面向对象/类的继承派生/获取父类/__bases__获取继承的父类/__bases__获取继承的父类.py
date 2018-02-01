# -*- coding:utf-8 -*-
class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

#获取类型的父类类型
print(A.__bases__)
print(B.__bases__)
print(C.__bases__)
print(D.__bases__)
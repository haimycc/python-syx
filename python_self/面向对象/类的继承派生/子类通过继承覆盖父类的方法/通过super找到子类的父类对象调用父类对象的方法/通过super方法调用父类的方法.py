# -*- coding:utf-8 -*-
class P(object):
    #重新定义了成员函数，在C类型的名字空间中有效
    def foo(self):
        print("Hi,I'm p-foo()")

p=P()
p.foo()



class C(P):
    #重新定义了成员函数，在C类型的名字空间中有效
    def foo(self):
        print("Hi,I'm c-foo()")

c=C()
c.foo()
#通过super函数，找到类型C的c成员的父类
#然后调用父类的方法
super(C,c).foo()

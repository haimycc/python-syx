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
        #找到C类型的父类，然后调用该父类对象的方法
        super(C,self).foo()
        print("Hi,I'm c-foo()")

c=C()
c.foo()
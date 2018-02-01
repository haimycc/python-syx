# -*- coding:utf-8 -*-
class C(object):
    #C可以调用
    def __call__(self, *args, **kwargs):
        print("hello,world")

#创建类对象
c=C()
#对类对象进行调用
c()
#判断类对象是否可以调用
print(callable(c))
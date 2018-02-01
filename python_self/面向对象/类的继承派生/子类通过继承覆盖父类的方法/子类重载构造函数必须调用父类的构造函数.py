# -*- coding:utf-8 -*-
class P(object):
    def __init__(self):
        print("parent:__init__")

class C(P):
    def __init__(self):
        #通过super找到父类的函数进行调用
        super(C,self).__init__()
        print("child:__init")

obj=C()

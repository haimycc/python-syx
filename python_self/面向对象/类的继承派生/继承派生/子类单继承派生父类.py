# -*- coding:utf-8 -*-
class parent(object):
    def parent_call(self):
        print("this is parent call:parent_call")

class son(parent):
    def son_call(self):
        print("this is son call:son_call")

#父类调用父类方法
p=parent()
p.parent_call()

#子类调用子类和父类方法
s=son()
s.parent_call()
s.son_call()
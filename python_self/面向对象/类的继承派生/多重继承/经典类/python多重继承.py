# -*- coding:utf-8 -*-
class P1:
    def foo(self):
        print("call p1-foo()")

class P2:
    def foo(self):
        print("call p2-foo()")
    def bar(self):
        print("call p2-bar()")

class C1(P1,P2):
    pass

class C2(P1,P2):
    def bar(self):
        print("call c2-bar()")

class GC(C1,C2):
    pass


gc=GC()
gc.foo()
gc.bar()

P2.bar(gc)

#查看新式类的查找顺序
print(GC.__mro__)

# -*- coding:utf-8 -*-
class P1(object):
    def foo(self):
        print("call p1-foo()")

class P2(object):
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

print(P1.__dict__)
print(P2.__dict__)
print(C1.__dict__)
print(C2.__dict__)
print(GC.__dict__)


print(P1().__dict__)
print(P2().__dict__)
print(C1().__dict__)
print(C2().__dict__)
print(GC().__dict__)
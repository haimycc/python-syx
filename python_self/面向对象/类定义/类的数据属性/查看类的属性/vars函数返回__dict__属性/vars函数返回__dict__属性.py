# -*- coding:utf-8 -*-
class MyClass(object):
    "this is Myclass"
    myVersion="1.0"
    def showMyVersion(self):
        print(self.myVersion)

obj=MyClass()
print(vars(obj))
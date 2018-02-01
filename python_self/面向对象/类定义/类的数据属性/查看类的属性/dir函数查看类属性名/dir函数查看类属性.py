# -*- coding:utf-8 -*-
class MyClass(object):
    "this is Myclass"
    myVersion="1.0"
    def showMyVersion(self):
        print(self.myVersion)

#查看类的属性,dir返回的是命名空间字典key名字
print(dir(MyClass))
print(MyClass.__doc__)

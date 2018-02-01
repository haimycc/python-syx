# -*- coding:utf-8 -*-
class MyClass(object):
    "this is Myclass"
    myVersion="1.0"
    def showMyVersion(self):
        print(self.myVersion)

#查看类的属性,dir返回的是命名空间字典，也就是完整的map容器
print(MyClass.__dict__)


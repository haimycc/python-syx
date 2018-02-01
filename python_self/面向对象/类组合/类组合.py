# -*- coding:utf-8 -*-
class IPhone:
    def __init__(self,num):
        self.PhoneNum=num
    def GetPhoneNum(self):
        return self.PhoneNum

class ICompute:
    def __init__(self,pc_type):
        self.Computer=pc_type
    def GetComputer(self):
        return self.Computer


class Person:
    def __init__(self,phone,pc):
        self.phone=phone
        self.computer=pc
    def GetPhone(self):
        return self.phone
    def GetComputer(self):
        return self.computer

#类组合
obj=Person(IPhone("13510260944"),ICompute("window"))
#获取类的依赖类
phone=obj.GetPhone()
pc=obj.GetComputer()
#调用其他类对象的成员函数
print(phone.GetPhoneNum())
print(pc.GetComputer())

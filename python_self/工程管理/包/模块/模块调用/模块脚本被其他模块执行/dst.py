#这个python模块之定义了类定义还有函数定义
#所以其他模块导入这个模块后，就可以根据这个模块的名字空间调用这个模块的可调用对象

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age

def GetName(obj):
    print(obj.GetName())

def GetAge(obj):
    print(obj.GetAge())
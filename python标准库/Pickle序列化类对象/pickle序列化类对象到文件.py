import pickle

class Person(object):
    def __init__(self,arg_name,arg_age):
        self.name=arg_name
        self.age=arg_age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age


obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())

#把类对象写入到文件中
fileName="zxp.pkl"
with open(fileName,"w") as f:
    strObj=pickle.dump(obj,f)

with open(fileName,"r") as f:
    obj2=pickle.load(f)
    print(obj2.GetName())
    print(obj2.GetAge())





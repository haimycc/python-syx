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
str=pickle.dumps(obj)
print(str)

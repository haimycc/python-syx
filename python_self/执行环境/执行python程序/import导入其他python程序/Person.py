class Person(object):
    def __init__(self,arg_name,arg_age):
        self.name=arg_name
        self.age=arg_age

    def GetName(self):
        return self.name

    def GetAge(self):
        return self.age


#如果这个py文件是主程序,
if __name__ == "__main__":
    obj=Person("zxp",30)
    print(obj.GetName())
    print(obj.GetAge())


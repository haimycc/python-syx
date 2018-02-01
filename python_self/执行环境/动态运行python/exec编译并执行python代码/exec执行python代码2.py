exec("""
with open("/etc/passwd","a+") as f:
    for line in f.readlines():
        print(line)

""")

class Person(object):
    def __init__(self,arg_nama,arg_age):
        self.name=arg_nama
        self.age=arg_age
    def GetName(self):
        return self.name
    def GetAge(self):
        return self.age

""")


obj=Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())


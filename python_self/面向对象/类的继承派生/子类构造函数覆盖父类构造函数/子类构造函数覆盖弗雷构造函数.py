class Parent(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Son(Parent):
    def __init__(self,name,age,addr):
        super(Son,self).__init__(name,age)
        self.addr=addr


obj=Son("zxp",30,"深圳市")
print(obj.name)
print(obj.age)
print(obj.addr)
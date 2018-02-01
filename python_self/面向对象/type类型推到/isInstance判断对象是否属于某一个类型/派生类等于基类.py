class Parent(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Son(Parent):
    def __init__(self,addr):
        self.addr=addr

#子类对象是子类类型和父类类型
obj=Son("汕头市")
if isinstance(obj,Parent) :
    print("obj is Parent type")

if isinstance(obj,Son):
    print("obj is Son type")


#父类对象不是子类类型
obj=Parent("zxp",30)
if isinstance(obj,Parent) :
    print("obj is Parent type")

if isinstance(obj,Son):
    print("obj is Son type")
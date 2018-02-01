class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

obj=Person("zxp",30)
print(repr(obj))
obj2=eval(repr(obj))
print(obj2.name)

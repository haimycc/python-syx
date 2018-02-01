class Parent(object):
    name="zxp"
    age=30

class Son(Parent):
    addr="深圳市区"


if issubclass(Son,Parent):
    print("son is subclass of Parent")
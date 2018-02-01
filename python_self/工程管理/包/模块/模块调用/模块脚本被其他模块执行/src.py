import dst

#调用导入模块的可调用对象
obj=dst.Person("zxp",30)
print(obj.GetName())
print(obj.GetAge())

#调用导入模块的可调用对象
dst.GetName(obj)
dst.GetAge(obj)
class WrapperClass:
    #类实例数据是另外一个类型
    def __init__(self,list):
        self.list=list
    def __repr__(self):
        return "self.list"
    def __str__(self):
        return str(self.list)
    #如果类实例对象找不到某一个属性，那么就跑去他的组合类型中查找该属性
    def __getattr__(self, attr):
        return getattr(self.list,attr)

obj=WrapperClass([0,1,2])
#WrapperClass本来是没有append属性的，现在他用的是组合类型的属性
obj.append(3)
obj.append(4)
print(obj)


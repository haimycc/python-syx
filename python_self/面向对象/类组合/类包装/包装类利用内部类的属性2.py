class WrapperClass:
    #类实例数据是另外一个类型
    def __init__(self,list):
        self.list=list
    def get(self):
        return self.list
    def __repr__(self):
        return "self.list"
    def __str__(self):
        return str(self.list)
    #如果类实例对象找不到某一个属性，那么就跑去他的组合类型中查找该属性
    def __getattr__(self, attr):
        return getattr(self.list,attr)

obj=WrapperClass([0,1,2,3,4,5,6,7,8,9,10])
#WrapperClass本来是没有append属性的，现在他用的是组合类型的属性
obj.append(11)
obj.append(12)
print(obj)

obj.pop()
print(obj)
print(obj.index(1))

#对于下标操作符，因为不在组合类的属性表中，所以我们无法通过getattr获取属性
#我们只可以取巧，通过get方法获取组合类，再调用组合类的方法
#print(obj[3])
# -*- coding:utf-8 -*-
class Student(object):
    #把类方法作为一个属性来使用
    @property
    def birth(self):
        #把真正的属性隐藏起来
        return self._birth
    #设置类的属性值
    @birth.setter
    def birth(self, value):
        self._birth = value
    #只读属性
    @property
    def age(self):
        return 2016 - self._birth


obj=Student()
#设置属性，其实就是调用方法来设置私有属性
obj.birth=1986
print(obj.birth)
print(obj.age)
# -*- coding:utf-8 -*-

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

obj=Student()
obj.birth=100
print(obj.birth)

print(obj.age)
#这里出错。因为没有setter方法。
#也就是这个方法转化的属性是只读属性。
obj.age=100



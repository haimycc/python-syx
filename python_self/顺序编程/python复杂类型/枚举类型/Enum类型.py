# -*- coding:utf-8 -*-
from enum import Enum
#Enum(枚举对象名
Month=Enum("Month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

#具体枚举类型
print(Month.Jan)
print(Month.Feb)
print(Month.Mar)
print(Month.Apr)
print(Month.May)
print(Month.Jun)
print(Month.Jul)


#
for name,member in Month.__members__.items():
    print(name,"=>",member,",",member.value)
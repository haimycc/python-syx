# -*- coding:utf-8 -*-
from string import Template
#这是一个字符串模板
s=Template("this is ${name} ,age is ${age} ,addr is ${addr}")
print(s.substitute(name="zxp",age=30,addr="广东省深圳市区"))


print(s.safe_substitute(name="zxp"))
print(s.safe_substitute(age=30))
print(s.safe_substitute(addr="广东省深圳市区"))
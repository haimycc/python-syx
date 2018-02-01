# -*- coding:utf-8 -*-
person=["name",["savings",100]]

#通过切片方式做到浅拷贝
hubby=list(person)
wife=list(person)

for x in person:
    print("id(x) in person is ",id(x))
for x in hubby:
    print("id(x) in hubby is ",id(x))
for x in wife:
    print("id(x) in wife is ",id(x))


wife[0]="zll"
hubby[0]="zxp"

for x in person:
    print("id(x) in person is ",id(x))
for x in hubby:
    print("id(x) in hubby is ",id(x))
for x in wife:
    print("id(x) in wife is ",id(x))
# -*- coding:utf-8 -*-

person=["name",["saving",100]]
#切片方法
hubby=person[:]
#工厂方法
wife=list(person)
#打印切片对象还有list对象的成员地址
print([id(x) for x in hubby])
print([id(x) for x in wife])


hubby[0]="joe"
wife[0]="jane"
print(hubby)
print(wife)
print([id(x) for x in hubby])
print([id(x) for x in wife])
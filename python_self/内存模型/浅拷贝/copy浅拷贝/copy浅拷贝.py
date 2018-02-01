# -*- coding:utf-8 -*-

import  copy

person=["name",["saving",100]]
#copy模块的前拷贝
hubby=copy.copy(person)
wife=copy.copy(person)
#打印切片对象还有list对象的成员地址
print([id(x) for x in hubby])
print([id(x) for x in wife])


hubby[0]="joe"
wife[0]="jane"
print(hubby)
print(wife)
print([id(x) for x in hubby])
print([id(x) for x in wife])
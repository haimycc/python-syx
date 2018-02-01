# -*- coding:utf-8 -*-
#元组解构
p=(4,5)
(e1,e2)=p
print("%d,%d"%(e1,e2))


#列表解构：
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
(e1,e2,e3,e4)=data
print("%s,%d,%d"%(e1,e2,e3))
print(e4)


#列表详细解构：
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
(e1,e2,e3,(e4,e5,e6))=data
print("%s,%d,%d,%d,%d,%d" % (e1,e2,e3,e4,e5,e6))


#如果元素个数不一致，那么会抛出异常
#x,y,z=(4,5)
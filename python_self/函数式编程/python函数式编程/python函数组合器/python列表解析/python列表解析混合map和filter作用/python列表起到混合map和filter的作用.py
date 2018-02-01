# -*- coding:utf-8 -*-
list=["zxp","zll","lqh"]
tuple=("zxp","zll","lqh")
map={"name":"zxp","age":30,"addr":"广东省深圳市区"}

after_list=["hello,"+item for item in list if item=="zxp"]
after_tuple=["hello,"+item for item in tuple]
after_map=["hello,"+item for item in map ]

for item in after_list:
    print(item)

for item in after_tuple:
    print(item)

#返回了enumeration
for key,value in enumerate(after_map):
    print("key:",key,",value:",str(value))
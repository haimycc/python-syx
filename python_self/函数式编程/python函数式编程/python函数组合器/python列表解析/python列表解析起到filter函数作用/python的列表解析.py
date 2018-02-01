# -*- coding:utf-8 -*-
list=["zxp","zll","lqh"]
tuple=("zxp","zll","lqh")

after_list=[item for item in list if item=="zxp"]
after_tuple=[item for item in list if item=="zxp"]

for item in after_tuple:
    print(item)

for item in after_list:
    print(item)
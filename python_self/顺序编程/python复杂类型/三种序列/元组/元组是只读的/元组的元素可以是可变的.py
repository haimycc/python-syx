# -*- coding:utf-8 -*-
#元组，元组的元素是list列表
tuple=([1,2,3,4],[5,6,7,8],[9,10])
#元组虽然不可变，但是元素时list可以是可变的
tuple[0][0]=4
tuple[0][1]=3
tuple[0][2]=2
tuple[0][3]=1
print(tuple)
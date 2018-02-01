# -*- coding:utf-8 -*-
#python map函数
after_map=map(lambda x:x+10,[1,2,3,4,5,6,7,8,9,10])
for element in after_map:
    print(element)

#列表解析做到map函数的效果
after_map2=[x+10 for x in range(1,11)]
for element in after_map2:
    print(element)
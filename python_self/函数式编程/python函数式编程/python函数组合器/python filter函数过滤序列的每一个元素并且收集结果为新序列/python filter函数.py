# -*- coding:utf-8 -*-
#filter函数过滤序列的元素组成新的序列
after_filter=filter(lambda x:x>0,[-5,-4,-3,-2,-1,0,1,2,3,4,5])
for element in after_filter:
    print(element)

#列表解析达到filter函数的功能
after_filter2=[x for x in range(-5,6) if x>0]
for element in after_filter2:
    print(element)
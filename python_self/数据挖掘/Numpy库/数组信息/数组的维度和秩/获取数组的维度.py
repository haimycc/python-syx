from numpy  import *

#创建【0,15）数组
#并且按照3个维度，每个位图长度为5
a = arange(15).reshape(3, 5)
print(a)
#打印数组维度
print(a.ndim)
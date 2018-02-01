from numpy  import *

#创建【0,15）数组
#并且按照3个维度，每个位图长度为5
a = arange(15).reshape(3, 5)
print(a)
#获取数组元素类型
print(a.dtype)

#获取数组元素类型
b = array([1.2, 3.5, 5.1])
print(b.dtype)



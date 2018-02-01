from numpy import *

#索引、切片和迭代，就像 列表 和其它Python序列
a = arange(10)**3
print(a)

#index
print(a[2])
#切片[2,5)
print(a[2:5])
#赋值,[0,6),每隔2个元素就赋值
a[:6:2] = -1000
print(a)
#逆序
print(a[ : :-1]) 


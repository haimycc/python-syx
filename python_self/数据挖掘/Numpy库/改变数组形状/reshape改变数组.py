from numpy import *

a=array([[ 7.,  5.],
       [ 9.,  3.],
       [ 7.,  2.],
       [ 7.,  8.],
       [ 6.,  8.],
       [ 3.,  2.]])

print(a)
#reshape 函数改变参数形状并返回它，而 resize 函数改变数组自身。
print(a.reshape(2,6))
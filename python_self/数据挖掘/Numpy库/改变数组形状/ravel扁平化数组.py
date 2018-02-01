from numpy import *

#一个数组的形状由它每个轴上的元素个数给出：
array=floor(10*random.random((3,4)))
print(array)
print(array.shape)
#扁平化数组
print(array.ravel())
print(array.ravel().shape)
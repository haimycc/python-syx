from numpy import *
#生成2维数组
array = floor(10*random.random((2,12)))
#把二维数组切分为3维
array2=hsplit(array,3)

print(array)
print(array2)
print(array2.shape)



from numpy import *

def f(x,y):
    return 10*x+y

#元素根据维度来定义
array= fromfunction(f,(5,4),dtype=int)
print(array)
#根据维度来找元素
print(array[2,3])
#找到某一列
#找到【0,5)行,第一列
print(array[0:5,1])
#找到【0,n)行，第一列
print(array[:,1])
#找到【1,3),所有列
print(array[1:3,:])
#索引为负数，那么就默认为整个切片
print(array[-1])
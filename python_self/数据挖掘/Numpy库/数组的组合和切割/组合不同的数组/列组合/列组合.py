from numpy import *

a=array([
    [0,1,2],
    [3,4,5],
    [6,7,8]])
print(a)

b=array([
    [0,2,4],
    [6,8,10],
    [12,14,16]])
print(b)

#水平组合
print()
c=column_stack((a,b))
print(c)
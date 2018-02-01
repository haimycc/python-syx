from numpy import *

array=arange(27).reshape(3,3,3)
print(array)
print()
#水平切割
print(hsplit(array,3))
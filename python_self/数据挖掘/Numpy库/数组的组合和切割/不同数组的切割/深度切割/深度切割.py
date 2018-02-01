from numpy import *

array=arange(27).reshape(3,3,3)
print(array)
#深度切割
print()
print(dsplit(array,3))
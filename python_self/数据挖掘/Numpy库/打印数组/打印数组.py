from numpy  import *

#当你打印一个数组，NumPy以类似嵌套列表的形式显示它，但是呈以下布局：
#	* 最后的轴从左到右打印
#	* 次后的轴从顶向下打印
#	* 剩下的轴从顶向下打印，每个切片通过一个空行与下一个隔开
#一维数组被打印成行，二维数组成矩阵，三维数组成矩阵列表。

a = arange(6)
print(a)

b = arange(12).reshape(4, 3)
print(b)

c = arange(24).reshape(2, 3, 4)
print(c)

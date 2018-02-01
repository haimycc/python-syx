from numpy import *

b=arange(24).reshape(2,3,4)
print(b.shape)
print(b)

#具体索引
print("具体索引")
print(b[0,1])
#递增索引
print("递增索引")
print(b[0,1,::2])

print("切片索引")
print(b[...,1])
print(b[:,:,1])

print("切片索引2")
#最后一列
print(b[0,:,-1])
print("切片索引3")
print(b[0,::2,-1])

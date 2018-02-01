import numpy as np
import pandas as pd

data=pd.Series(
    np.random.rand(10),
    #创建多层次索引
    index=[
        ["a","a","a","b","b","b","c","c","d","d"],
        [1,2,3,1,2,3,1,2,2,3]
    ]
)
print(data)
print()
print("打印所有索引")
print(data.index)
print()

print("根据层次化索引找到具体数据:第一维度")
print(data['a'])
print()

print("根据层次化索引找到具体数据:第一+第二维度")
print(data['b':'c'])
print()

print("根据层次化索引找到具体数据:第二维度")
print(data[:,2])
print()

#通过unstack,可以把多重索引转化为DataFrame
frame=data.unstack()
print(frame)
#通过stack,可以把DataFrame转化为多重索引的Series
new_data=frame.stack()
print(new_data)
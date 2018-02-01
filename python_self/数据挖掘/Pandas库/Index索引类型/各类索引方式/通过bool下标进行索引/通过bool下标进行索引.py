import pandas as pd
import numpy as np

data=pd.DataFrame(
    #数据集
    np.arange(16).reshape((4,4)),
    #行index
    index=["Ohio","Colorado","Utah","New York"],
    #列index
    columns=["one","two","three","four"]
)
print(data)
print()
#获取bool索引
print(data>5)
print()
data[data>5]=1
print(data)
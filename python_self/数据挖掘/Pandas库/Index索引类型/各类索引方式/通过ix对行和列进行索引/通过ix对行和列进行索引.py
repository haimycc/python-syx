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
#找到一行两列
#ix可以获取行索引和列索引的交集
print(data.ix["Colorado",["one","three"]])


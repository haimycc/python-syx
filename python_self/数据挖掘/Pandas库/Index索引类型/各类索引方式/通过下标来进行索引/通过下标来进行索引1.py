import pandas as pd
import numpy as np

obj=pd.Series(np.arange(4.),index=["a","b","c","d"])
print(obj)
#通过下标来搜索
print("通过下标来搜索")
print(obj["a"])
print(obj["b"])
#通过下标列表来进行搜索
print("通过下标列表来进行搜索")
print(obj[["a","b","c"]])
#通过个别下标来进行搜索
print("通过个别下标来进行搜索")
print(obj[[1,3]])
#通过条件判断
print("通过条件判断")
print(obj[obj<2])

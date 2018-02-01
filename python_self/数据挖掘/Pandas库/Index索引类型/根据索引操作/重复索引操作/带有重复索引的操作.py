import numpy as np
import pandas as pd

obj=pd.Series(
    range(5),
    index=["a","a","b","b","c"]
)
print(obj)
#判断index是否唯一
print(obj.index.is_unique)
print()

#根据索引获取值
print(obj["a"])
import numpy as np
import pandas as pd

obj=pd.Series(range(4),index=["d","a","b","c"])
print(obj)
print()
#根据index进行降序排列
new_obj=obj.sort_index(ascending=False)
print(new_obj)
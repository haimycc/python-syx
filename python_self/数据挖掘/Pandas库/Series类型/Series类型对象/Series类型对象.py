import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#series只有numpy多维数组和索引集组成
obj=pd.Series([4,7,-5,3])
print(obj)

#获取Series的数据集
print(obj.values)

#获取Series的索引集
print(obj.index)
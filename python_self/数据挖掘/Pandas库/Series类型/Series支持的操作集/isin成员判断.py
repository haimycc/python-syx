import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj=pd.Series(['a','b','c','a','b','c'])
#获取series的唯一值
unique=obj.unique()
print(unique)
print()
#获取series的分组计数
counts=obj.value_counts()
print(counts)
print()
#判断object是否在这个mask中
mask=obj.isin(['b','c','d','e'])
print(mask)
print()
#判断符合条件的seriese
print(obj[mask])
print()
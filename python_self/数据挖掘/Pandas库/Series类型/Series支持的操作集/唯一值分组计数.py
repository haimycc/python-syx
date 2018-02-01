import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj=pd.Series(['a','b','c','a','b','c'])
#获取series的唯一值
unique=obj.unique()
print(unique)

#获取series的分组计数
counts=obj.value_counts()
print(counts)
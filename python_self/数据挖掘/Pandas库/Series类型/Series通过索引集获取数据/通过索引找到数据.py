import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj=pd.Series([1,2,3,4,5,7],index=['a','b','c','d','e','f'])
print(obj)
print(obj['a'])
obj['a']=100
print(obj)
#通过多个索引找多个元素
print(obj[['a','b','c']])


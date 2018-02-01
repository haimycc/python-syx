import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obj=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj)
print()
#遍历Series对象的data数据集
for data in obj:
    print(data)
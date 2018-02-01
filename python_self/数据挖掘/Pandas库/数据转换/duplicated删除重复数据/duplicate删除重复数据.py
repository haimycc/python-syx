import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame({
    "k1":["one"]*3+["two"]*4,
    "k2":[1,1,2,3,3,4,4]
})
print(data)
print()

#判断前面是否有重复行
print(data.duplicated())
print()

#删除重复行,保留第一行
print(data.drop_duplicates())
print()

#删除重复行,保留最后一行
print(data.drop_duplicates(["k1","k2"]),take_last=True)
print()
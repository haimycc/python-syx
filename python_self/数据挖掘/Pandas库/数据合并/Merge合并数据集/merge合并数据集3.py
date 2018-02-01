import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1=pd.DataFrame({
    "lkey":['b','b','a','c','a','a','b'],
    "data1":range(7)
})
df2=pd.DataFrame({
    "rkey":['a','b','d'],
    "data2":range(3)
})

print(df1)
print()
print(df2)
print()
#根据指定的key进行链接
df3=pd.merge(df1,df2,left_on="lkey",right_on="rkey")
print(df3)

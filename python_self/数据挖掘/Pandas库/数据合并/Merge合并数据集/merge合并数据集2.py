import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1=pd.DataFrame({
    "key":['b','b','a','c','a','a','b'],
    "data1":range(7)
})
df2=pd.DataFrame({
    "key":['a','b','d'],
    "data2":range(3)
})

print(df1)
print()
print(df2)
print()
#innserlian链接
df3=pd.merge(df1,df2,on="key")
print(df3)
print()
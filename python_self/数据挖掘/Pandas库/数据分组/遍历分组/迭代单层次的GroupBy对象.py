import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.DataFrame({
    "key1":["a","a","b","b","a"],
    "key2":["one","two","one","two","one"],
    "data1":np.random.randn(5),
    "data2":np.random.randn(5)
})

groups=df.groupby("key1")
print(groups)
print(groups.size())

for name,group in df.groupby("key1"):
    print(name)
    print(group)


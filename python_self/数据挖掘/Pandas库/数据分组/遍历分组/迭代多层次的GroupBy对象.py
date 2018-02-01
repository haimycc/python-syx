import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.DataFrame({
    "key1":["a","a","b","b","a"],
    "key2":["one","two","one","two","one"],
    "data1":np.random.randn(5),
    "data2":np.random.randn(5)
})

#元祖第一个元素是由键值组
for (k1,k2),group in df.groupby(["key1","key2"]):
    print(k1,k2)
    print(group)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.DataFrame({
    "key1":["a","a","b","b","a"],
    "key2":["one","two","one","two","one"],
    "data1":np.random.randn(5),
    "data2":np.random.randn(5)
})

print(df)
print()
#分组
groupd=df["data1"].groupby(df["key1"])
print(groupd)
#分组
print(groupd.size())
print()
#分组汇总
groupd2=df["data1"].groupby([df["key1"],df["key2"]]).mean()
print(groupd2)
print()
#分组汇总2
unstack=groupd2.unstack()
print(unstack)
print()
#
states=np.array(["Ohio","California","California","Ohio","Ohio"])
years=np.array([2005,2005,2006,2005,2006])
rest=df["data1"].groupby([states,years]).mean()
print(rest)
print()
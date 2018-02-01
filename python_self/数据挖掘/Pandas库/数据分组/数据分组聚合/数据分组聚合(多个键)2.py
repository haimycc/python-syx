import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.DataFrame({
    "key1":["a","a","b","b","a"],
    "key2":["one","two","one","two","one"],
    "data1":np.random.randn(5),
    "data2":np.random.randn(5)
})

means=df["data1"].groupby([df["key1"],df["key2"]]).mean()
print(means)
print()

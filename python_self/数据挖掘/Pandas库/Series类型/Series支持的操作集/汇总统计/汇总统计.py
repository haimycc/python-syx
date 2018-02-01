import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.DataFrame(
    [
        [1.4,np.nan],
        [7.1,-4.5],
        [np.nan,np.nan],
        [0.75,-1.3]
    ],
    index=['a','b','c','d'],
    columns=["one","two"]
)
#统计汇总,对行统计汇总
print(df.sum())
print()
#统计汇总,对列统计汇总
print(df.sum(axis=1))
print()






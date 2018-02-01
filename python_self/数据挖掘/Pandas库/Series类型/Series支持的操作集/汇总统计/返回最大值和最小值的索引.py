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

#找到每一列最大值和最小值的索引
print(df.idxmin())
print(df.idxmax())
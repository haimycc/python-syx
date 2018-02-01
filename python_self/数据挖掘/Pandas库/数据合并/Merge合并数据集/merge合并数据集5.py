import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


left=pd.DataFrame(
    {
        "key1":["foo","foo","bar"],
        "key2":["one","two","one"],
        "lval":[1,2,3]
    }
)
right=pd.DataFrame(
    {
        "key1":["foo","foo","bar","bar"],
        "key2":["one","one","one","two"],
        "rval":[4,5,6,7]
    }
)
#全连接
df=pd.merge(left,right,on=["key1","key2"],how="right")
print(df)
print()

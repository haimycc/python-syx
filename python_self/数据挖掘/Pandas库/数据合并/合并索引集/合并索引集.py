import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

left1=pd.DataFrame(
    {
        "key":["a","b","a","a","b","c"],
        "value":range(6)
    }
)
right1=pd.DataFrame(
    {
        "group_val":[3.5,7]
    },
    index=["a","b"]
)
print(left1)
print()
print(right1)
print()
#左边用列做键，右边用index做键
dp=pd.merge(left1,right1,left_on="key",right_index=True)
print(dp)
print()
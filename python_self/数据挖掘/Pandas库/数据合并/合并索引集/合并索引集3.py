import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lefth=pd.DataFrame(
    {
        "key1":["Ohio","Ohio","Ohio","Nevada","Nevada"],
        "key2":[2000,2001,2002,2001,2002],
        "data":np.arange(5)
    }
)

righth=pd.DataFrame(
    np.arange(12).reshape((6,2)),
    index=[
        ["Nevada","Nevada","Ohio","Ohio","Ohio","Ohio"],
        [2001,2000,2000,2000,2001,2002]
    ],
    columns=["event1","event2"]
)

print(lefth)
print()
print(righth)
print()

#必须以多重层的建作为key
df3=pd.merge(
    lefth,righth,
    left_on=["key1","key2"],
    right_index=True
)
print(df3)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


left=pd.DataFrame(
    [
        [1,2],
        [3,4],
        [5,6]
    ],
    index=["a","c","e"],
    columns=["Ohio","Nevada"]
)

right=pd.DataFrame(
    [
        [7,8],
        [9,10],
        [11,12],
        [13,14]
    ],
    index=["b","c","d","e"],
    columns=["Missouri","Alabama"]
)

#join合并多个相同或者相识索引
pd3=left.join(right,how="outer")
print(pd3)
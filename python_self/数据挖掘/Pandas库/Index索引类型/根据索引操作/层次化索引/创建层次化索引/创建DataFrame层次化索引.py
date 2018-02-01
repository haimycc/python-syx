import numpy as np
import pandas as pd


frame=pd.DataFrame(
    np.arange(12).reshape((4,3)),
    index=[
        ["a","a","b","b"],
        [1,2,1,2]
    ],
    columns=[
        ["Ohio","Ohio","Colorado"],
        ["Green","Red","Green"]
    ]
)
print(frame)
print()
#给多重索引,每一个索引都加名字
frame.index.names=["key1","key2"]
frame.columns.names=["state","color"]
print(frame)
#根据index索引,找到分组
print(frame["Ohio"])
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
print()
#把key1和key2这2个索引进行交换
new_frame=frame.swaplevel("key1","key2")
print(new_frame)
print()
#key1和key2交互后再排序
new_frame2=new_frame.sortlevel("key2")
print(new_frame2)
print()

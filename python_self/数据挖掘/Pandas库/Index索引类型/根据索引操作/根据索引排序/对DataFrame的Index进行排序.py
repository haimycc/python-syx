import numpy as np
import pandas as pd

frame=pd.DataFrame(
    np.arange(8).reshape((2,4)),
    index=["three","one"],
    columns=["d","a","b","c"]
)

#对index进行排序
new_frame=frame.sort_index()
print(new_frame)
print()
#对columns进行排序
new_frame2=frame.sort_index(axis=1)
print(new_frame2)
import numpy as np
import pandas as pd

obj=pd.Series(
    np.arange(5.),
    index=["a","b","c","d","e"]
)
print(obj)

#Series删除具体索引指定的轴
new_obj=obj.drop("c")
print(new_obj)

#Series删除具体索引指定的轴
new_obj2=obj.drop(["c","d"])
print(new_obj2)




















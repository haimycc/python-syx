import numpy as np
import pandas as pd

obj=pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=["Ohio","Colorado","Utah","NewYork"],
    columns=["one","two","three","four"]
)
print(obj)
print()

#默认的话，删除的是index
new_obj=obj.drop(["Colorado","Ohio"])
print(new_obj)
print()
#如果要删除columns
new_obj2=obj.drop(["two"],axis=1)
print(new_obj2)
print()
#如果要删除columns
new_obj3=obj.drop(["two","four"],axis=1)
print(new_obj3)

import pandas as pd
import numpy as np

obj=pd.Series(
    [4.5,7.2,-5.3,3.6],
    index=["d","b","a","c"])
print(obj)

#重新建立索引,对于没有存在的,用Null代替
obj2=obj.reindex(["a","b","c","d","e"])
print(obj2)

#如果是默认值填充
obj3=obj.reindex(["a","b","c","d","e"],fill_value=0)
print(obj3)

#用前面的值进行填充
obj4=obj.reindex(["a","b","c","d","e"],method='ffill')
print(obj4)
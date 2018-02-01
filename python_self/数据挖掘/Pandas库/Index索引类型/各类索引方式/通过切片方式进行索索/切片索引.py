import pandas as pd
import numpy as np

obj=pd.Series(np.arange(4.),index=["a","b","c","d"])
print(obj)
print()
#切片索引,和python不同，是包括【】,而不是[)
print(obj["b":"c"])
#设置数组
obj["b":"c"]=5
print(obj)


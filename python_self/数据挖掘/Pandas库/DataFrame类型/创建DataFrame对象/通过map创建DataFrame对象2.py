import pandas as pd
import numpy as np

#通过map容器方式创建DataFrame
data={
    'state':["a","b","c","d"],
    'year':[2000,2001,2002,2003],
    'pop':[1,2,3,4]
}
#根据dict字典创建DataFrame数据结构
#注意key会就是列索引
#如果我们指定了columns,那么就按照columns的顺序进行排列
frame=pd.DataFrame(data,columns=['pop',"state","year"])
print(frame)
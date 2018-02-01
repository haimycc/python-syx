import pandas as pd
import numpy as np

#通过map容器方式创建DataFrame
data={
    'state':{200:"a",201:"b",202:"c",204:"d"},
    'year':{200:2000,201:2001,202:2002,203:2003},
    'pop':{200:1,201:2,202:3,203:4}
}
#根据dict字典创建DataFrame数据结构
#注意key会就是列索引
#内嵌dict的key就是行索引
#如果我们指定了columns,那么就按照columns的顺序进行排列
frame=pd.DataFrame(data,columns=['pop',"state","year"])
print(frame.T)
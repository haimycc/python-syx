import pandas as pd
import numpy as np

#通过map容器方式创建DataFrame
data={
    'state':{"one":"a","two":"b","three":"c","four":"d"},
    'year':{"one":2000,"two":2001,"three":2002,"four":2003},
    'pop':{"one":1,"two":2,"three":3,"four":4}
}
#根据dict字典创建DataFrame数据结构
#注意key会就是列索引
#自动添加行索引
frame=pd.DataFrame(data,columns=["year","state","pop","debt"],index=["one","two","three","four","five"])
print(frame)

#新增列名
frame["new_column"]= "True"
print(frame)
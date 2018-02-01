import pandas as pd
import datetime
import numpy as np

#給2个日期，然后date_range就是生产了时间序列,递增时间为1天
index=pd.date_range("4/12/2012","6/1/2012")
print(index)
print()
#往后延10天
index=pd.date_range(start="4/12/2012",periods=10)
print(index)
print()
#往前延10天
index=pd.date_range(end="6/1/2012",periods=10)
print(index)
print()
#生成每月最后一个工作日
index=pd.date_range("1/1/2000","12/1/2000",freq="BM")
print(index)
print()
#保留时间信息
index=pd.date_range("5/2/2012 12:56:31",periods=5)
print(index)
print()
#传入年月
longer_ts=pd.Series(np.random.randn(1000),
                    index=pd.date_range("1/1/2000",periods=1000))
print(longer_ts)
print()
#日期范围
dates=pd.date_range("1/1/2000",periods=100,freq="W-WED")
long_df=pd.DataFrame(np.random.randn(100,4),
                     index=dates,
                     columns=["one","two","three","four"]
                     )
print(long_df)
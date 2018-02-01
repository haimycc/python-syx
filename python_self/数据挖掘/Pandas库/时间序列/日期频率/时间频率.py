from pandas.tseries.offsets import Hour,Minute
import pandas as pd

#1小时频率
hour=Hour()
#4小时时间频率
hour4=Hour(4)
#时间范围,4个小时
index=pd.date_range("1/1/2000","1/3/2000 23:59:59",freq="4h")
print(index)
print()

#时间范围,4小时30分
index=pd.date_range("1/1/2000","1/3/2000 23:59:59",freq="4h30min")
print(index)
print()

#时间范围,通过制定日期
index=pd.date_range("1/1/2012","9/1/2012",freq="WOM-3FRI")
print(index)
print()
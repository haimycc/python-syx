import pandas as pd
import datetime


stamp=datetime.datetime(2011,1,3)
#字符串
print(str(stamp))
#格式化
strTime=stamp.strftime("%Y-%m-%d")
print(strTime)
#格式化
value="2011-01-03"
strTime=datetime.datetime.strftime(value,"%Y-%m-%d")

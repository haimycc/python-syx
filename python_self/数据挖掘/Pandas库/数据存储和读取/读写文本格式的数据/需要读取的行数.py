# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#只读取3行
frame=pd.read_csv("./repaymentInfo.csv",nrows=3)
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
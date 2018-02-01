# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#跳过3行
frame=pd.read_csv("./repaymentInfo.csv",skiprows=[0,1,2])
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
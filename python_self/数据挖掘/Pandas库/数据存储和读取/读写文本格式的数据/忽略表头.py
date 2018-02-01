# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#忽略表头
frame=pd.read_csv("./repaymentInfo.csv",header=None)
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
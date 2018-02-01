# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#把csv格式转化为dataframe
frame=pd.read_csv("./repaymentInfo.csv")
#print(frame)
#print(frame.columns)
#print()
#print(frame.index)
#print()
#print(frame.values)
#print()

frame2=pd.read_table("./repaymentInfo.csv",sep=",")
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
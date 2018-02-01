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

#去掉index
frame.to_csv("./copy.csv",index=False)
#只选择特定的行
frame.to_csv("./copy2.csv",index=False,columns=["还款表ID"])

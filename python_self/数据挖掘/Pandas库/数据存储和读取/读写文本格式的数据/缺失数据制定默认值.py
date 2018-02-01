# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

sentinels={"投资人应收本金":["foo","NA"]}
frame=pd.read_csv("./repaymentInfo.csv",na_values=sentinels)
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
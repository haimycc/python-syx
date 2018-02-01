# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#忽略表头
frame=pd.read_csv("./repaymentInfo.csv",names=["还款表ID1","标ID1","标名称1","借款人姓名1","借款人手机号1","第几期还款1","借款人应还本金1","投资人应收本金1","差额"])
#print(frame)
print(frame.columns)
print()
print(frame.index)
print()
print(frame.values)
print()
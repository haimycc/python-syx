# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

#把csv格式转化为dataframe
frame=pd.read_csv("./repaymentInfo.csv",chunksize=10)
for piece in frame:
    print(piece.index)
    print(piece.values)
    print()
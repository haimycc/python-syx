import pandas as pd
import numpy as np

xls_file=pd.ExcelFile("用户13278763202的回款记录.xlsx")
frame= xls_file.parse("Sheet1")
#获取列索引
print(frame.columns)
print()
#获取行索引
print(frame.index)
print()
#获取数据集
print(frame.values)
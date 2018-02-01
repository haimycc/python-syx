import pandas as pd
import numpy as np


frame=pd.DataFrame(
    np.arange(9).reshape((3,3)),
    index=["a","c","d"],
    columns=["Ohio","Texas","Califonia"]
)
print(frame)
print()

#如果只传入一个序列,那么就会重新索引行
frame2=frame.reindex(["a","b","c","d"])
print(frame2)
print()
#可以用columns对列索引进行重新索引
states=["Texas","Utah","Califonia"]
frame3=frame.reindex(columns=states)
print(frame3)
print()
#利用ix进行信息索引
frame4=frame.ix[["a","b","c","d"],states]
print(frame4)



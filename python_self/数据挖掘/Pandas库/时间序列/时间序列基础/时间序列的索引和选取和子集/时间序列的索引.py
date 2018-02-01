import pandas as pd
import numpy as np
from datetime import datetime

dates = [
    datetime(2011,1,2),
    datetime(2011,1,5),
    datetime(2011,1,7),
    datetime(2011,1,8),
    datetime(2011,1,10),
    datetime(2011,1,12)
]

ts=pd.Series(np.random.rand(6),index=dates)
print(ts)
print()
#根据时间索引
print(ts["1/2/2011"])
print()
#根据时间索引
print(ts["20110102"])
print()




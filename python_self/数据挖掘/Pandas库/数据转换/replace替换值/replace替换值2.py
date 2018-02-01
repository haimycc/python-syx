import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(
    [1,-999,2,-999,-1000,3]
)
print(data)
print()
#替换seriese或者dataFrame中的值
print(data.replace([-999,-1000],[999,1000]))

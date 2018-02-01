import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#map容器对象
mapObj={
    "a":1,
    "b":2,
    "c":3
}

state=['apple',"banana","bear"]
obj=pd.Series(mapObj,index=state)
print(obj)
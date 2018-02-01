import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame(
    {
        "food":["bacon","pulled pork","bacon","Pastrami","beef","Bacon","pas","honey","lox"],
        "ounces":[4,3,12,6,7.5,8,3,5,6]
    }
)

print(data)
print()

#对dataFrame中的数据进行map映射
print(data["food"].map(lambda x:1))
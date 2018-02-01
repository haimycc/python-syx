import numpy as np
import pandas as pd

df=pd.DataFrame(
    np.random.rand(4,3),
    index=["a","a","b","b"]
)
print(df)
print()

print(df.ix['b'])


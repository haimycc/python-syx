import numpy as np
import pandas as pd

frame=pd.DataFrame(
    {
        "a":[4,-7,-3,2],
        "b":[0,1,0,1]
    }
)
print(frame)
print()
print(frame.sort_index(by="b"))
print()
print(frame.sort_index(by=["a","b"]))

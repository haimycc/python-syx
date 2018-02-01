import numpy as np
import pandas as pd

frame=pd.DataFrame(
    {
        "a":range(7),
        "b":range(7,0,-1),
        "c":["one","one","one","two","two","two","two"],
        "d":[0,1,2,0,1,2,3]
    }
)

print(frame)
print()

#把column索引变为index索引
frame2=frame.set_index(["c","d"])
print(frame2)
print()

frame3=frame2.reset_index()
print(frame3)
print()
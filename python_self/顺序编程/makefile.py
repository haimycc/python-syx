# -*- coding:utf-8 -*-
import os
ls=os.linesep

while True:
    if os.path.exists(fname):
        print("Error: %s already exist",fname)
    else:
        break

all=[]
print("enter line:")
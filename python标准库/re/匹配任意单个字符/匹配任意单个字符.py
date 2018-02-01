from re import *

anyend=".end"
m=match(anyend,"bend")
if m is not None:
    print(m.group())

m=match(anyend,"end")
if m is not None:
    print(m.group())


m=match(anyend,"\nend")
if m is not None:
    print(m.group())

m=search(".end","The end.")
if m is not None:
    print(m.group())
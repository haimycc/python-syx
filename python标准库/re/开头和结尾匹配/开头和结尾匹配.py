from re import *

m=search("^The","The end.")
if m is not None:
    print(m.group())


m
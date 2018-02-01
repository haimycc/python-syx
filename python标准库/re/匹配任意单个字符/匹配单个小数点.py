from re import *

m=match("3\.14","3.14")
if m is not None:
    print(m.group())


m=match("3\.14","3014")
if m is not None:
    print(m.group())
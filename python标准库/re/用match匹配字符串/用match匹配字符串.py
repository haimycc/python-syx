from re import *

m=match("foo","foo")
if m is not None:
    print(m.group())
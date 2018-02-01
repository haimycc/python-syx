from re import *

m=match("foo","food on the table,foood")
if m is not None:
    print(m.group())

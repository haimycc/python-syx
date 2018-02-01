from re import *

m=match("(\w\w\w)-(\d\d\d)","abc-123")
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
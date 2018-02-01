from re import *

m=match("\w\w\w-\d\d\d","abc-123")
if m is not None:
    print(m.group())


m=match("\w\w\w-\d\d\d","abc-xyz")
if m is not None:
    print(m.group())

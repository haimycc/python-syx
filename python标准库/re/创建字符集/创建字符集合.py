from re import *

m=match("[cr][23][dp][o2]","c3po")
if m is not None:
    print(m.group())

m=match("[cr][23][dp][o2]","c2do")
if m is not None:
    print(m.group())


m=match("r2d2|c3po","r2d2")
if m is not None:
    print(m.group())

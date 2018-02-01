from re import *

m=match("bat|bet|bit","bat")
if m is not None:
    print(m.group())

m=match("bat|bet|bit","blt")
if m is not None:
    print(m.group())

m=match("bat|bet|bit","He bit me")
if m is not None:
    print(m.group())

#search匹配上
m=search("bat|bet|bit","He bit me")
if m is not None:
    print(m.group())
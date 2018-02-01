import types
if isinstance((1,2,3),tuple):
    print("(1,2,3) is tuple")

if isinstance([1,2,3,],tuple):
    print("[1,2,3,] is tuple")

if isinstance((1,2,3),list):
    print("(1,2,3) is list")

if isinstance([1,2,3],list):
    print("[1,2,3] is list")


if isinstance((1,2,3),(list,tuple)):
    print("(1,2,3) is list or tuple")

if isinstance([1,2,3],(list,tuple)):
    print("[1,2,3] is list or tuple")

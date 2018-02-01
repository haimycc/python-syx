from re import *

try:
    match("foo","this is not match").group()
except:
    print("not match")

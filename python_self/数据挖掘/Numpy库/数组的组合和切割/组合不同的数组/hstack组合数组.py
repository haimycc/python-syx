from numpy import *

a = floor(10 * random.random((2, 2)))
b = floor(10*random.random((2,2)))
c=hstack((a,b))

print(a)
print("...")
print(b)
print("...")
print(c)
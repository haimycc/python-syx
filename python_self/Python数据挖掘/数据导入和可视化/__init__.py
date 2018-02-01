
from numpy import genfromtxt, zeros
# read the first 4 columns
data = genfromtxt('local.csv',delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt('local.csv',delimiter=',',usecols=(4),dtype=str)

print(data)
print(target)
print(set(target))


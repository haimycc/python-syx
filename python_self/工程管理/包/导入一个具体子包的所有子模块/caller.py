#from 具体子包下面的*模块
# 这个*模块其实就是这个具体子模块下面的__all__变量指定的模块
from www.baidu.com import *


obj1=Person.Person("zxp",30)
obj2=Student.Student("zxp",30)
print(obj1.GetName())
print(obj2.GetName())
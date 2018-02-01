#导入包里面某个具体模块的具体名字
from www.google.Hello import *
from www.baidu.Hello import *

#因为2个包都有SayHello这个函数，所以2个包的顺序非常重要
#因为后面的包会把前面的包的名字覆盖掉
SayHello()



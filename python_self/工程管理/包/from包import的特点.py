#from一个包，然后导入他的子包，子包再导入他们的子包，通过__all__
#通过这条指令，包里面的所有子包都被导入了,通过__all__
#最底层的子包导入具体模块名,通过__all__
from www.baidu import *
from www.baidu.other import *

#通过接下去的路径就可以访问到具体的模块了
ByeBye.ByeBye()
Fuck.Fuck()
Hello.SayHello()
other.other()




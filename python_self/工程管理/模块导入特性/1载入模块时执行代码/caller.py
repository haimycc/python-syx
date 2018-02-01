#导入www这包
import www
#导入www.baidu这包
from www import baidu

#因为导入包会指向这个包下面的__init__.py文件
#所以我们就可以获取在这个文件下执行的代码
print(www.www)
print(baidu.baidu)
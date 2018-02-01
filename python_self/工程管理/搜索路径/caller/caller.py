import sys
#获取路径
print(sys.path)
#把搜索和查找路径加入到sys.path中
sys.path.append("D:\\git_code\\python_self-python\\python_self\\工程管理\\搜索路径\\")

#现在可以导入该具体路径了
from www.baidu.com import Hello
Hello.Hello()
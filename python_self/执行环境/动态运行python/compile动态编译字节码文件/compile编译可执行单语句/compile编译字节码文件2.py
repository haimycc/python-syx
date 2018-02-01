# -*- coding:utf-8 -*-
#注意tab和空格影响编译

#compile的几个参数：
#arg1：表示python字符串代码
#arg2：表示编译后的字节码文件
#arg3：表示python代码属于哪种模式
#single，表示单一可执行python语句
eval_code=compile("print(\"hello,world\")","eval.pyc","single")
print(eval(eval_code))

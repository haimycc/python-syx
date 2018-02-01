# -*- coding:utf-8 -*-
#注意tab和空格影响编译

#compile的几个参数：
#arg1：表示python字符串代码
#arg2：表示编译后的字节码文件
#arg3：表示python代码属于哪种模式
#exec，表示可执行python语句组。
eval_code=compile("""
for i in range(10):
        print(i)

""","","exec")
exec(eval_code)




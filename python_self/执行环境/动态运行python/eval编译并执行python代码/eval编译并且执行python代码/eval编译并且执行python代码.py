# -*- coding:utf-8 -*-
#注意tab和空格影响编译
#编译为字节码
code = compile("""
for i in range(1,10):
    print(i)

""", "", "single")
#执行字节码
eval(code)
# -*- coding:utf-8 -*-
#compile的几个参数：
#arg1：表示python字符串代码
#arg2：表示编译后的字节码文件
#arg3：表示python代码属于哪种模式
#eval，那么表示这个是python的可求值表达式
eval_code=compile("100+200","eval.pyc","eval")
print(eval(eval_code))

# -*- coding:utf-8 -*-
def highFunction(f,arg1,arg2,arg3,arg4,arg5):
    return f(arg1,arg2,arg3,arg4,arg5)
#高阶函数
result=highFunction(lambda a,b,c,d,e:a+b+c+d+e,1,2,3,4,5)
print(result)
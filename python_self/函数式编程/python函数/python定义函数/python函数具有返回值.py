# -*- coding:utf-8 -*-
def function():
    return 0

print("result is ",function())


def function2(n):
    result=[]
    a,b=0,1
    while a<n :
        result.append(a)
        a,b=b,a+b
    return result

print(function2(100))




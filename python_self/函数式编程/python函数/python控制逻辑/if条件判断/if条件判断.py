# -*- coding:utf-8 -*-
def IsXOne(arg):
    if arg<0 :
        print(arg,"<0")
    elif arg==0 :
        print(arg,"=0")
    elif arg==1 :
        print(arg,"==1")
    else:
        print("arg is ",arg)
    return arg

IsXOne(-1)
IsXOne(0)
IsXOne(1)
IsXOne(2)
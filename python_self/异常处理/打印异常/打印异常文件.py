# -*- coding:utf-8 -*-
import traceback

try:
    raise ArithmeticError
except:
    print("begin print Except")
    f=open("./exceptFile","a+")
    traceback.print_exc(file=f)
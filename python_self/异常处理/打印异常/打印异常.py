# -*- coding:utf-8 -*-
import traceback

try:
    raise ArithmeticError
except:
    print("begin print Except")
    traceback.print_exc()
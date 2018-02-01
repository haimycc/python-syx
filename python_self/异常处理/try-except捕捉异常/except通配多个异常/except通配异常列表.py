# -*- coding:utf-8 -*-
try:
    raise IOError("this is IOError")
except (IOError,NameError,ZeroDivisionError):
    print("there is a error")
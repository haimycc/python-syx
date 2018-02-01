# -*- coding:utf-8 -*-
try:
    raise NameError("this is IOError")
except (IOError,NameError,ZeroDivisionError) as e:
    print("there is a error")

# -*- coding:utf-8 -*-
#IOError
try:
    raise IOError("this is IOError")
except IOError:
    print("this is IOError")
except NameError:
    print("this is NameError")
except ZeroDivisionError:
    print("this is ZeroDivisionError")
except :
    print("other except")

#NameError
try:
    raise NameError("this is NameError")
except IOError:
    print("this is IOError")
except NameError:
    print("this is NameError")
except ZeroDivisionError:
    print("this is ZeroDivisionError")
except :
    print("other except")


#ZeroDivisionError
try:
    raise ZeroDivisionError("this is ZeroDivisionError")
except IOError:
    print("this is IOError")
except NameError:
    print("this is NameError")
except ZeroDivisionError:
    print("this is ZeroDivisionError")
except :
    print("other except")



# -*- coding:utf-8 -*-
try:
    pass
except:
    print("this is except")
else:
    #else只有在没有俘获到异常的情况下才会触发执行
    print("this is not except")
finally:
    print("finally begin")


try:
    raise IOError("this is IOError")
except:
    print("this is except")
else:
    #else只有在没有俘获到异常的情况下才会触发执行
    print("this is not except")
finally:
    print("finally begin")
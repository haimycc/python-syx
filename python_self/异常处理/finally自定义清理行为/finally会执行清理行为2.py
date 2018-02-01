# -*- coding:utf-8 -*-
try:
    #抛出IOError错误
    raise IOError("this is IOError")
except (IOError,BlockingIOError) as obj:
    #获取一个异常类对象
    print(obj)
finally:
    #进入finally块
    print("this is finally block")
# -*- coding:utf-8 -*-
try:
    raise BlockingIOError("this is BlockingIOError")
except BaseException as obj:
    print(obj)
finally:
    print("this is finally block")



try:
    raise AssertionError("this is AssertionError")
except BaseException as obj:
    print(obj)
finally:
    print("this is finally block")



try:
    raise BufferError("this is BufferError")
except BaseException as obj:
    print(obj)
finally:
    print("this is finally block")


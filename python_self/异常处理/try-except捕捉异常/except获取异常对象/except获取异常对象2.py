# -*- coding:utf-8 -*-
try:
    raise BlockingIOError("this is BlockingIOError")
except (AssertionError,BlockingIOError,BufferError) as obj:
    print(obj)
finally:
    print("this is finally block")



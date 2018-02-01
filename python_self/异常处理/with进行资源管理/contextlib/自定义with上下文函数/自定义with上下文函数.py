# -*- coding:utf-8 -*-
import time
from contextlib import contextmanager

@contextmanager
def Resource():
    #yield是在with操作前执行
    print("resource enter")
    #yield的只就是as 后面的只
    yield 1
    #yield是在with操作后执行
    print("resource exit")


with Resource() as r:
    time.sleep(10)
    print(r)

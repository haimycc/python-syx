# -*- coding:utf-8 -*-
import time

class Resource(object):
    def __enter__(self):
        print("resource enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("resource exit")


with Resource() as r:
    time.sleep(10)






# -*- coding:utf-8 -*-
import time
from contextlib import nested

class Resource(object):
    def __enter__(self):
        print("resource enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("resource exit")



with nested(Resource(),Resource(),Resource()) as (r1,r2,r3):
    time.sleep(4)
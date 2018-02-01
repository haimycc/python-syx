# -*- coding:utf-8 -*-
class Person:
    #错误，python要求__init__必须放回None
    def __init__(self):
        return 1

obj=Person()

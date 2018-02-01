#!/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

#退出操作1
oldHandler=getattr(sys,'exitfunc',None)
def exitHandler1(preHandler=oldHandler):
    #我们的操作
    print("exitHandler1")
    #获取老的handler
    if preHandler is not None and callable(preHandler):
        preHandler()

sys.exitfunc=exitHandler1

#退出操作2
oldHandler=getattr(sys,'exitfunc',None)
def exitHandler2(preHandler=oldHandler):
    #我们的操作
    print("exitHandler2")
    #获取老的handler
    if preHandler is not None and callable(preHandler):
        preHandler()

sys.exitfunc=exitHandler2

#退出操作3
oldHandler=getattr(sys,'exitfunc',None)
def exitHandler3(preHandler=oldHandler):
    #我们的操作
    print("exitHandler3")
    #获取老的handler
    if preHandler is not None and callable(preHandler):
        preHandler()

sys.exitfunc=exitHandler3

sys.exit()


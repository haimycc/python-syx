# -*- coding:utf-8 -*-
import sys

try:
    #sys.exit会抛出SystemExit异常
    #如果我们俘获异常，那么python程序就不会退出。
    sys.exit(0)
except SystemExit:
    print("SystemEixt happen")
finally:
    print("finally:SystemExit happen")

print("this is after sys.exit(0)")
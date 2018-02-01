# -*- coding:utf-8 -*-
import sys


print("this is before sys.exit(0)")
#抛出SystemExit异常导致程序退出
#SystemExit异常可以不被俘获
sys.exit(0)
print("this is after sys.exit(0)")
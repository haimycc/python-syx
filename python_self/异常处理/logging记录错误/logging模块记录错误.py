# -*- coding:utf-8 -*-
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        #同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
        logging.exception(e)

main()
print('END')

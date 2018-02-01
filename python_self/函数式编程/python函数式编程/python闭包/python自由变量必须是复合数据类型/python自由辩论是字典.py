# -*- coding:utf-8 -*-
def OuterFunction():
    dict={
        "name":"zxp",
        "age":30,
        "addr":"广东省深圳市区"
    }
    def Inner():
        print(dict)
    return Inner

f=OuterFunction()
f()
f()
f()


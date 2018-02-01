# -*- coding:utf-8 -*-


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action,"\n")
    print("if you put", voltage, "volts through it.","\n")
    print("E's", state, "!\n")
    return

#定义map字典对象
mymap={
    "voltage":"zxp",
    "state":"zxp",
    "action":"zxp"
}

#拆分map对象到函数参数
parrot(**mymap)

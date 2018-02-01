# -*- coding:utf-8 -*-
def function():
    #设定num为0
    num=0
    #匿名函数的默认参数是外部变量0
    f=lambda arg: arg+num
    print(f(0))
    #修改匿名函数的外部变量
    num=10
    #发现lambda函数在定义时,外部变量不没有绑定到lambda中
    print(f(0))


function()
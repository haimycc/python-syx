# -*- coding:utf-8 -*-
num=100
num2=200

def function():
    #全局变量必须和局部变量名字不同
    global num2
    num2=300



print(num)
print(num2)
function()
print(num2)

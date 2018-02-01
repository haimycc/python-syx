# -*- coding:utf-8 -*-
name="before"
age=30

#函数默认参数是在定义时是就确定的
#函数默认参数定以后不会被修改
def function(arg1=name,arg2=age):
    print("name is ",arg1,",age is ",arg2)
    return
function()

name="after"
age=0
function()

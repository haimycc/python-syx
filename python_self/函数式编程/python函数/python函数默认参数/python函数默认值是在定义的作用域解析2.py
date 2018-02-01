# -*- coding:utf-8 -*-
mylist=[]

#默认参数是一个含有指针的结构体
#通过这个指针，我们还是修改了该结构体
def function(num,arg=mylist):
    arg.append(num)
    return

function(1)
function(2)
function(3)
print(mylist)



def function2(num,arg=None):
    if arg is None:
        arg=[]
    arg.append(num)
    return
function2(1)
function2(2)
function2(3)

# -*- coding:utf-8 -*-
def hellocounter (name):
    count=0
    #闭包
    def counter():
        count+=1
        print('Hello,',name,',',str(count)+' access!')
    return counter

function=hellocounter("zxp")
function()
function()
function()
function()
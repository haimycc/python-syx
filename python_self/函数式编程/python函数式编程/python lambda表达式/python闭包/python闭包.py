# -*- coding:utf-8 -*-
def hellocounter (name):
    count=[0]
    #闭包
    def counter():
        count[0]+=1
        print('Hello,',name,',',str(count[0])+' access!')
    return counter

function=hellocounter("zxp")
function()
function()
function()
function()
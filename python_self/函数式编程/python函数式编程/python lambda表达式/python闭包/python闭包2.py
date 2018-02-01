# -*- coding:utf-8 -*-
def hellocounter (name):
    count=[0]
    def counter():
        count[0]+=1
        print('Hello,',name,',',str(count[0])+' access!')
    return counter

#闭包失效
hellocounter("zxp")()
hellocounter("zxp")()
hellocounter("zxp")()
hellocounter("zxp")()
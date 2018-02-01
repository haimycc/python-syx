# -*- coding:utf-8 -*-
def function():
    for num in range(2,10):
        if num%2==0 :
            print("Found an even number",num)
            continue
        print("Found a number ",num)
    return


function()
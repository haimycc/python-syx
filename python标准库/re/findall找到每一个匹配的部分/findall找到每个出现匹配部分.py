from re import *

#如果匹配上，那么返回列表
m=findall("car","car bcar ccar")
if m is not None:
    print(m)

#如果没有匹配上，那么就是返回空列表
m=findall("car"," ")
if m is not None:
    print(m)
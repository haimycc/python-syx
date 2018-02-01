# -*- coding:utf-8 -*-

def function(name,age,*info,**infos):
    print("name is "+name)
    print("age is "+str(age))
    print("info is "+str(info))
    print("infos is "+str(infos))

function("zxp",30,
         #对list和tuple容器进行*解引用
         *["汕头市","父母"],
         #对map容器进行**解引用
         **{"infos_name":"zxp","infos_age":30,"infos_addr":"广东省汕头市",}
         )
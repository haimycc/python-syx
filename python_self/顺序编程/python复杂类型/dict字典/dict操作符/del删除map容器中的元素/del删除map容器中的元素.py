# -*- coding:utf-8 -*-
mymap={
    "name":"zxp",
    "age":30,
    "addr":"广东省深圳市区"
}
print(mymap)
#删除map容器对象中的某一个元素
del mymap["name"]
print(mymap)

#删除整一个map对象，所以无法再继续访问
del mymap
print(mymap)
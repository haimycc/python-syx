# -*- coding:utf-8 -*-
mymap={
    "name":"周晓鹏",
    "age":30,
    "addr":"广东省深圳市",
}
print(mymap["name"])
print(mymap["age"])
print(mymap["addr"])


for key in mymap.keys():
    print("key is %s,value is %s" % (key,mymap[key]))
# -*- coding:utf-8 -*-
import urllib.parse

aDict={
    "name":"周晓鹏",
    "age":30,
}

#把一个map对象转化为url键值对,并且有url编码
print(urllib.parse.urlencode(aDict))



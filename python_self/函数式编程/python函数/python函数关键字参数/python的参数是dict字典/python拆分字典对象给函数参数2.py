# -*- coding:utf-8 -*-

def function(name,age,address):
    print("name is ",name)
    print("age is ",age)
    print("address is ",address)
    return

mymap={
    "address":"中国",
    "age":30,
    "name":"zxp"
}

#拆分字典对象，只可以覆盖关键字参数，而没法覆盖位置参数
function(**mymap)
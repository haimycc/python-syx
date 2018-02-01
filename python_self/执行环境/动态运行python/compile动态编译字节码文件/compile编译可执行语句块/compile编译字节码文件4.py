# -*- coding:utf-8 -*-
#注意tab和空格影响编译

eval_code=compile("""
f = open("/etc/password","a+")
for line in f.readlines():
    print(line)

""","","exec")
exec(eval_code)
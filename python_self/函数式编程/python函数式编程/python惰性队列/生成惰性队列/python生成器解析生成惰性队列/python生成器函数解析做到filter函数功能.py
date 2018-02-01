# -*- coding:utf-8 -*-
#生成惰性队列的函数
def Generate():
    yield "zxp"
    yield "lqh"
    yield "zll"

#通过不断调用惰性队列的函数，不断生成惰性元素
after_generage=(item for item in Generate() if item=="zxp")
for item in after_generage:
    print(item)
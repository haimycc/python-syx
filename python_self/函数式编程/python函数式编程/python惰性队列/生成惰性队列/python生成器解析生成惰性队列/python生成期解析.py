# -*- coding:utf-8 -*-
#生成惰性队列
def Generate():
    yield "zxp"
    yield "lqh"
    yield "zll"

#生成器调用生成惰性队列的函数，然后通过迭代的方式，每次获取一个惰性元素
after_generate=(item for item in Generate())

for item in after_generate:
    print(item)



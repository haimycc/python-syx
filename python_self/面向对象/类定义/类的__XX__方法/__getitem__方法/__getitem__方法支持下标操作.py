# -*- coding:utf-8 -*-
class Fib(object):
    #类支持下标操作符
    #下标返回的值由我们的函数控制
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f=Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[100])
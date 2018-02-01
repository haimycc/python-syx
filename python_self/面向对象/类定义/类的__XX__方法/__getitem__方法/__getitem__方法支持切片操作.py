# -*- coding:utf-8 -*-
class Fib(object):
    def __getitem__(self, n):
        # n是索引
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
         # n是切片
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

obj=Fib()
print(obj[0:5])
print(obj[:10])

# -*- coding:utf-8 -*-
class Fib(object):
     # 初始化两个计数器a，b
    def __init__(self):
        self.a, self.b = 0, 1

    # 实例本身就是迭代对象，故返回自己
    def __iter__(self):
        return self

    # 计算下一个值
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # 退出循环的条件
        if self.a > 100000:
            #这种异常不需要处理
            raise StopIteration()
        # 返回下一个值
        return self.a


for n in Fib():
    print(n)

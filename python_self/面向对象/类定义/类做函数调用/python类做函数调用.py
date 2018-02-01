# -*- coding:utf-8 -*-
class Person(object):
    def __call__(self, *args, **kwargs):
        print("I'm callable!called with args:",args,kwargs)

#生成类实例对象
object=Person()
print(callable(object))
#类对象做函数调用
object()
#类对象做函数调用，需要的是元组变参和map变参
object("hello,world","byebye",arg3="hello,world",arg4="byebye")
# -*- coding:utf-8 -*-

class Person(object):
    def __call__(self, *args, **kwargs):
        print("this is Person, args is ",args,"kwargs is ",kwargs)

obj=Person()
print(callable(obj))

obj("arg1","arg2",arg3="arg3",arg4="arg4")

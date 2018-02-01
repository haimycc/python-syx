# -*- coding:utf-8 -*-

class Person(object):
    def __len__(self):
        return 0

obj=Person()
print(obj.__len__())
if obj is False:
    print("obj is False")
# -*- coding:utf-8 -*-
#0
print(0 is False)
#""
print("" is False)
#''
print('' is False)
#""""""
print("""""" is False)
#[]
print([] is False)
#()
print(() is False)
#{}
print({} is False)

#class
class Person(object):
    def __len__(self):
        return 0

print(Person() is False)

#上面表示不同的类型和False是不同的

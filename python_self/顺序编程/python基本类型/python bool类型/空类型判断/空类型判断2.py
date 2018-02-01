# -*- coding:utf-8 -*-
#0
if 0:
    print("0 is true")
if "":
    print(""" "" is true""")
if '':
    print(""" '' is true""")

if """""":
    print(""" is true""")

if []:
    print("[] is true")

if ():
    print("() is true")

class Person(object):
    def __len__(self):
        return 0

if Person():
    print("Person() is true")

#上面的判断都是False
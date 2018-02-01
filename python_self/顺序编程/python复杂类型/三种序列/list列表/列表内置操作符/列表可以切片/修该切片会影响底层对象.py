# -*- coding:utf-8 -*-
#修改切片会影响底层对象
letters=['a','b','c','d','e','f']
letters[2:5]=["C","D","E"]
print(letters)

letters[:]=[]
print(letters)
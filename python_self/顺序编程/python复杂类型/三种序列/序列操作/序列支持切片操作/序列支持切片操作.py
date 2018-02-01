# -*- coding:utf-8 -*-
list=[1,2,3]
tuple=(1,2,3)
str="123"

splice1=list[0:]
splice2=tuple[0:]
splice3=str[0:]

splice1[0]=3
#splice2[0]=3
#splice3[0]="3"

print(splice1)
print(splice2)
print(splice3)
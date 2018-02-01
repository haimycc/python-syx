# -*- coding:utf-8 -*-
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
#获取前面的元素
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

#获取最后一个元素
*other,last=record
print(other)
print(last)

#获取中间元素
first,*middle,last=record
print(first)
print(middle)
print(last)

#获取第一个元素
first,*last=record
print(first)
print(last)


#字符串分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname)
print(*fields)
print(homedir)
print(sh)
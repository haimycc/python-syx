# -*- coding:utf-8 -*-
record = ('ACME', 50, 123.45, (12, 18, 2012))
#把多余的变量丢弃
name, *_, (*_, year) = record
print(name)
print(year)
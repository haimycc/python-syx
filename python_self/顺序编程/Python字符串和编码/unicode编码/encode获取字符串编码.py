# -*- coding:utf-8 -*-
print("ABC".encode("ascii"))
print("ABC".encode("utf-8"))
print("中文".encode("utf-8"))

#utf-8编码的字节流解码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))

#非utf8编码的字节流解码会导致问题
#print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("ascii"))
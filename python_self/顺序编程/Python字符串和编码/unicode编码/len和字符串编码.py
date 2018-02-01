# -*- coding:utf-8 -*-
#如果是字符，那么len获取的是字符的长度
print(len("ABC"))
print(len("中文"))

#如果是字节流，那么len获取的是字节流的长度
print(len(b"ABC"))
print(len(b"\xe4\xb8\xad\xe6\x96\x87"))
print (len("中文".encode("utf-8")))


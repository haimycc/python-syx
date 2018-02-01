# -*- coding:utf-8 -*-
import time

class Resource(object):
    def __enter__(self):
        print("resource enter")
        #创建资源
        self.file=open("zxp.txt",mode="w")
        #返回资源
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("resource exit")
        #释放资源
        self.file.close()


with Resource() as f:
    f.write("hello,world")




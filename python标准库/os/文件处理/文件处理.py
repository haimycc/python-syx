#-*- coding: UTF-8 -*-

import os


#判断/tmp是不是路径
for tmpdir in ("/tmp",):
    if os.path.isdir(tmpdir):
        print(tmpdir,"is a dir")

if os.path.isabs("/tmp"):
    #更改路径
    os.chdir("/tmp")
    #获取路径
    cwd=os.getcwd()
    print(cwd)

#打印当前目录下的文件
print(os.listdir(os.getcwd()))

#建立文件
file=open("/tmp/zxp","w")
file.write("hello,world")
file.write("byebye\n")
file.close()
print(os.listdir(os.getcwd()))

#给文件更名
os.rename("/tmp/zxp","/tmp/newzxp")
print(os.listdir(os.getcwd()))


#读文件
print("*** displaying file contents:")
file = open("/tmp/newzxp")
allLines = file.readlines()
file.close()
for eachLine in allLines:
    print(eachLine)

#删除文件
os.remove("/tmp/newzxp")
print(os.listdir(os.getcwd()))

#创建目录
os.mkdir("/tmp/newdir")
print(os.listdir(os.getcwd()))

#删除目录
os.rmdir("/tmp/newdir")
print(os.listdir(os.getcwd()))

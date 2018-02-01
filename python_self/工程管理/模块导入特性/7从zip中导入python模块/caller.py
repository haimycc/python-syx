#!-*- coding:UTF-8 -*-

#导入一个python中的一个子包
#from www import *
import sys
#把zip文件加入到sys.path中
sys.path.append("www.zip")

from www import google
from www import baidu

print(google.google)
print(baidu.baidu)
#方式1：import必须截止到具体的模块
import www.baidu.Hello
import www.google.Hello

#因为是import，而不是from xx import yy
#所有这个就需要具体模块名
www.baidu.Hello.SayHello()
www.google.Hello.SayHello()
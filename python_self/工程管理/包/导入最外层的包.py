import www

#导入最外层的包，还是无法通过限定符来访问模块的内部符号
www.baidu.Hello.SayHello()
www.google.Hello.SayHello()
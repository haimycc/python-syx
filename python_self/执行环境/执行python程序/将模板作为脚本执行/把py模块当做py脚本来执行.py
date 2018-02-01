#这部分的内容，只有在模块是main模块，也就是可执行的主模块的时候才会被执行
#如果模块只是一个普通的，等待被其他模块导入的，那么
#这部分的py代码就不会被执行
if __name__=="__main__" :
    print("process when py module is main module")
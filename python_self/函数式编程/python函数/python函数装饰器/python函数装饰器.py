# -*- coding:utf-8 -*-
#函数装饰器
def log(func):
    #函数装饰器会返回一个内部函数，这个内部函数的参数是“被装饰的函数”
    #这个内部函数的参数类型就是“被装饰的函数”的参数类型
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#表明now是"被装饰的函数",log是装饰器函数
@log
def now():
    print('2015-3-25')

#log(now)
now()

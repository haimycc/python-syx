# -*- coding:utf-8 -*-
class WrapMe(object):
    def __init__(self,obj):
        self.__data=obj
    def get(self):
        return self.__data
    def __repr__(self):
        return "self.__data"
    def __str__(self):
        return str(self.__data)
    #如果__getattribute__方法找不到属性
    #那么就默认使用__getattr__方法
    #__getattr__方法调用getattr方法，跑去其他类对象的命名空间查找属性
    def __getattr__(self, attr):
        return getattr(self.__data,attr)


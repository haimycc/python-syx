# -*- coding:utf-8 -*-
import Person


#如果这个py文件是主程序,
if __name__ == "__main__":
    obj=Person.Person("lqh",30)
    print(obj.GetName())
    print(obj.GetAge())
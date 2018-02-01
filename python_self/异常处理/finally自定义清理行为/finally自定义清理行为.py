# -*- coding:utf-8 -*-
try:
    raise IOError("this is IoError")
except:
    print("this is IOError")
finally:
    print("finally begin")


try:
    pass
except:
    print("this is IOError")
finally:
    print("finally begin")
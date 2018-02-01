#代理模式：
class closing(object):
    # help doc here
    def __init__(self, thing):
        self.thing = thing
    #代理方法
    def __enter__(self):
        return self.thing
    #代理方法
    def __exit__(self, *exc_info):
        self.thing.close()


#被代理的对象
class ClosingDemo(object):
    def __init__(self):
        self.acquire()

    def acquire(self):
        print('Acquire resources.')

    def free(self):
        print('Clean up any resources acquired.')
    #被代理的方法
    def close(self):
        self.free()


with closing(ClosingDemo()):
    print('Using resources')


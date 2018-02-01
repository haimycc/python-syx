import atexit

def exit0(*args,**kwargs):
    print("exit0")
    for arg in args:
        print(" "*4,arg)
    for item in kwargs.items():
        print(" "*4,item)


def exit1():
    print("exit1")
    #raise Exception,"exit1"

def exit2():
    print("exit2")


atexit.register(exit0,*[1,2,3],**{"name":"zxp","age":30})
atexit.register(exit1)
atexit.register(exit2)


@atexit.register
def exit3():
    print("exit3")

if __name__=="__main__" :
    pass
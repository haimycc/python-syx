import asyncio


# @asyncio.coroutine把一个generator标记为coroutine类型，然后，我们就把这个coroutine扔到EventLoop中执行。
# hello()会首先打印出Hello world!，然后，yield from语法可以让我们方便地调用另一个generator。
# 由于asyncio.sleep()也是一个coroutine，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。
# 当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
@asyncio.coroutine
def hello():
    print("hello world")
    r=yield from asyncio.sleep(10)
    print("hello again")

#eventloop
loop=asyncio.get_event_loop()
#执行coroutinue
loop.run_until_complete(hello())
loop.close()
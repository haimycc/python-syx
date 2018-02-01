import threading
import time

lock=threading.Lock()
def run_thread():
    for i in range(10000):
        lock.acquire()
        try:
            print(threading.current_thread().name+" is doing")
            raise BlockingIOError("lock is lose")
        except BlockingIOError:
            pass
        finally:
            lock.release()


for i in range(10):
    t=threading.Thread(target=run_thread)
    t.start()




time.sleep(10)
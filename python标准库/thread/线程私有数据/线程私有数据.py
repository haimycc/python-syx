import threading

#创建线程私有数据
local_school=threading.local()

#获取线程私有数据
def process_student():
    std=local_school.student
    age=local_school.age
    print("hello,%s %d is (in %s)" % (std,age,threading.current_thread().name))

#每一个线程给自己的线程私有数据进行绑定对象
def process_thread(name,age):
    local_school.student=name
    local_school.age=age
    process_student()


t1=threading.Thread(target=process_thread,args=("zxp",30),name="Thread-A")
t2=threading.Thread(target=process_thread,args=("lqh",31),name="Thread-B")

t1.start()
t2.start()

t1.join()
t2.join()



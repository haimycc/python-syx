from collections import defaultdict

class Task:
    def __init__(self,name):
        self.name=name

    def send(self,msg):
        print("{} get {}" % (self.name,msg))

class Exchange:
    def __init__(self):
        self._subscribers=set()

    def attach(self,task):
        self._subscribers.add(task)

    def detach(self,task):
        self._subscribers.remove(task)

    def send(self,msg):
        for task in self._subscribers:
            task.send(msg)





if __name__ == '__main__':
    task_a=Task("A")
    task_b=Task("B")

    exc =

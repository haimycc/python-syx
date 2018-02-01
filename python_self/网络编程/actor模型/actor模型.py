# -*- coding:utf-8 -*-
from queue import Queue
from threading import Thread,Event


#signal to notify exit
class ActorExit(Exception):
    pass

#actor模型
class Actor:
    def __init__(self):
        '''
        Queue队列
        Returns:
        '''
        self._mailbox=Queue()

    def send(self,msg):
        '''
        Args:
            发送消息给Queue队列
            msg: send a message to the actor
        Returns:
        '''
        self._mailbox.put(msg)

    def recv(self):
        '''
            receive an incoming message
        Returns:
        '''
        #get message
        msg=self._mailbox.get()
        #msg is notify
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        '''
            发送关闭的消息给Queue队列
            close the actor,thus shutting it down
        Returns:
        '''
        self.send(ActorExit)

    def start(self):
        '''
            start cocurrent execution
        Returns:
        '''
        self._terminated=Event()
        #开启守护线程
        t=Thread(target=self._bootstrap)
        t.daemon=True
        t.start()

    #
    def join(self):
        self._terminated.wait()

    #守护线程执行run函数
    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    #actor start
    def run(self):
        '''
        Run method to be implemented by the user
        '''
        while True:
            msg = self.recv()


#actor to print
class PrintActor(Actor):
    def run(self):
        while True:
            msg=self.recv()
            print("Got:",msg)



if __name__ == '__main__':
    p=PrintActor()
    p.start()
    p.send("Hello")
    p.send("World")
    p.close()
    p.join()



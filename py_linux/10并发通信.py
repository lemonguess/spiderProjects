'''多进程间互相通信
通过创建服务器进程，再由服务器进程开辟字典空间/列表空间
进行数值传递'''
import multiprocessing
# dict = {'a':10,'b':20}
# mg = multiprocessing.Manager()#创建一个服务器进程，并返回与其通信的管理器
#
#
# def fun():
#     global dict
#     dict.update({'a':1,'b':2})
#
# dict = mg.dict() #通过公共进程开辟字典空间
# p1 = multiprocessing.Process(target=fun)
# p1.start()
# p1.join()  #让主进程等待子进程结束再结束
# print(dict)

'''多线程的互相通信——始终在同一个进程之中，是共享一个内存空间的
应该考虑如何避免资源争夺
'''
import time
start_time = time.clock()
import threading
var = 10
lock = threading.Lock()
def fun1():
    global var
    lock.acquire()
    for i in range(1000000):

        var += 1
    lock.release()


def fun2():
    global var
    lock.acquire()
    for i in range(1000000):

        var -= 1
    lock.release()


t1 = threading.Thread(target=fun1)
t1.start()
t2 = threading.Thread(target=fun2)
t2.start()
t1.join()
t2.join()
print(var)
end_time = time.clock()
print(end_time-start_time)

'''用队列实现生产者和消费者模型'''
# import threading
# import queue
# import time
# q=queue.Queue(4)
#
# #消费者
# class Con(threading.Thread):
#     def __init__(self,q):
#         super().__init__()
#         self.queue = q
#
#     def run(self):
#         while True:
#             item = self.queue.get()
#             print('消费者消费了%s'%item)
#
# #生产者
# class Pro(threading.Thread):
#     def __init__(self,q):
#         super().__init__()
#         self.queue = q
#
#     def run(self):
#         import random
#         while True:
#             item = random.randint(0,100)
#             self.queue.put(item)
#             print('生产者生产了%s' %item)
# pr=Pro(q)
# cu=Con(q)
#
# pr.start()
# cu.start()






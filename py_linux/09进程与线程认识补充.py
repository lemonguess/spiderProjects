# import time
# import multiprocessing  # 导入多进程模块
# import threading  # 导入多线程模块
#
#
# def new_time():
#     # 格式化时间
#     return time.asctime(time.localtime(time.time()))
#
#
# def func(x):
#     print('inner_start:', new_time())
#     print(x)
#     time.sleep(5)  # 休眠5秒钟模拟io耗时
#     print('inner_end:', new_time())
#
#
# print('outer_start:', new_time())
# p1 = multiprocessing.Process(target=func, args=(2, ))  # 实例化一个进程对象
#
# print('befor start:',p1.pid)
# p1.start()  # 开启子进程
# print('after start:',p1.pid)
# # t1 = threading.Thread(target=func, args=(3, ))  # 实例化一个线程对象
# # t1.start()  # 开启子线程
#
#
# time.sleep(5)
# res = input('现在有任务正在进行，是否确认关闭（Y/N）？')
# if res == 'Y':
#     p1.terminate() #强制终止子进程
# else:
#     p1.join() #主进程等待子进程结束
# print('outer_end:', new_time())
#
#
# # import socket
# # import multiprocessing
# #
# # server = socket.socket()
# # server.bind(('127.0.0.1', 8989))
# # server.listen(10)
# #
# #
# # def handle(conn):
# #     """子进程帮助处理数据"""
# #     while True:
# #         recv_data = conn.recv(1024)
# #         if recv_data:
# #             print(recv_data)
# #             conn.send(recv_data)
# #         else:
# #             conn.close()
# #             break
# #
# #
# # while True:
# #     # 生成对等套接字
# #     conn, address = server.accept()
# #     process = multiprocessing.Process(target=handle, args=(conn, ))
# #     process.start()


import redis
import multiprocessing

class RedisProcess(multiprocessing.Process):
    def __init__(self,db,key,values):
        super().__init__()
        self.db = redis.Redis(db=db) #连接Redis
        self.key = key
        self.values = values

    def set(self): #添加数据的方法
        self.db.set(self.key,self.values)

    def get(self):
        return self.db.get(self.key)

    def run(self):  #start 开启进程之后，由run方法进行具体的代码调用
        print(multiprocessing.current_process())
        self.set()

r1 = RedisProcess(1,'moran','18')
r2 = RedisProcess(2,'mr','28')
r1.start()
r2.start()


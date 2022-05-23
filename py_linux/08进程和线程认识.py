# #1. 进程
# import time
# import multiprocessing #导入多进程模块
# import threading #导入多线程模块
#
#
# def new_time():
#     #格式化时间
#     return time.asctime(time.localtime())
#
# def func():
#     print('inner_start:',new_time())
#     time.sleep(5) #休眠5秒 模拟io耗时
#     print('iner_end:',new_time())
#
# print('outer_start:',new_time())
# p1 = multiprocessing.Process(target = func) #实例化一个进程对象
# p1.start() #开启子进程
# t1 = threading.Thread(target=func,args=(3, ))#实例化一个线程对象
#
# time.sleep(5)
# func()
# print('outer_end:',new_time())




#多进程的实现——子进程
# import socket
# import multiprocessing
#
# server = socket.socket()
# server.bind(('127.0.0.1',8989))
# server.listen(10)
#
# def handle(conn):
#     '''子进程帮助处理数据'''
#     while True:
#         recv_data = conn.recv(1024)
#         if recv_data:
#             print(recv_data)
#             conn.send(recv_data)
#         else:
#             conn.close()
#             break
#
# while True:
#     '''生成对等套接字'''
#     conn ,address = server.accept()
#     process = multiprocessing.Process(target=handle, args=(conn,))
#     process.start()




#多线程的实现——子线程
import threading
import socket

server = socket.socket()
server.bind(('127.0.0.1',8989))
server.listen(10)

def handle(conn):
    while True:
        data_recv = conn.recv(1024)
        if data_recv:
            print(data_recv)
            conn.send(data_recv)
        else:
            conn.close()
            break
while True:
    conn , address = server.accept()
    t = threading.Thread(target=handle,args=(conn,))
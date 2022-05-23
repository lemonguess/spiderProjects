# import socket
# server = socket.socket()

# server.setblocking(False)  # 设置非阻塞套接字 需要在绑定ip之前
# server.bind(('127.0.0.1', 8989))
# server.listen(10)

# while True:
#     try:
#         conn, address = server.accept()
#         data = conn.recv(1024)
#         conn.send(data)
#     except BlockingIOError:
#         pass
#     except Exception as e:
#         print('发生了异常，异常信息为', e)

# all_conn = []
# while True:
#     try:
#         conn, address = server.accept()
#         conn.setblocking(False)  # 设置非阻塞IO
#         all_conn.append(conn)
#     except BlockingIOError:
#         pass
#     except Exception as e:
#         print('发生了异常，异常信息为', e)
#
#     for conn in all_conn:  # 遍历所有套接字，进行数据处理
#         try:
#             recv_data = conn.recv(1024)
#             if recv_data:
#                 print(recv_data)
#                 conn.send(recv_data)
#             else:
#                 conn.close()
#                 all_conn.remove(conn)
#         except BlockingIOError:
#             pass
#         except Exception as e:
#             print('发生了异常，异常信息为', e)



import socket
import selectors  # 导入复用器模块

epoll_select = selectors.EpollSelector()  # 实例化一个epoll复用器对象
# default_select = selectors.DefaultSelector()  # 实例化默认复用器

server = socket.socket()
server.bind(('127.0.0.1', 8989))
server.listen(10)


def f_recv(conn):
    recv_data = conn.recv(1024)
    if recv_data:
        print(recv_data)
        conn.send(recv_data)


def f_accept(server):
    conn, address = server.accept()
    epoll_select.register(conn, selectors.EVENT_READ, f_recv)


# selectors.EVENT_READ 只要检测到有时间发生 就进行函数回调
epoll_select.register(server, selectors.EVENT_READ, f_accept)


while True:
    events = epoll_select.select()  # 不断查询有没有事件发生 如果有就查询出来 然后进行函数回调
    print(events)
    for key, mask in events:
        func = key.data  # 注册进去的函数体
        conn = key.fileobj  # 注册进去的对象
        func(conn)
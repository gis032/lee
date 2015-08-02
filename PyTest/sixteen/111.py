#-*- coding:utf-8 -*-
import socket,traceback,os
from threading import *

host = ''
port = 51423     #监听所有的接口

#接受消息的线程
def handlerecv(clientsock):
    print (currentThread().getName())
    print (clientsock.getpeername())
    while True:
        data = clientsock.recv(4096)
        if not len(data):
            break
        print (data)
    clientsock.close()

#发送消息的线程
def handlesend(clientsock):
    while True:
        data = raw_input(">")
        data = data + "\n";   #加上换行，好看一点。
        clientsock.sendall(data)
    #关闭连接
    clientsock.close()

#建立套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

while True:
    try:
        clientsock,clientaddr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    t = Thread(target = handlerecv,args=[clientsock])
    t.setDaemon(1)
    t.start()

    r = Thread(target = handlesend,args=[clientsock])
    r.setDaemon(1)
    r.start()
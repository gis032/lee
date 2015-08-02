#encode=utf8
'''
Created on 2015年7月26日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/sixteen/server1.py

(
'''
from socket import * 
from time import ctime,sleep
HOST=""
PORT=28888
BZ = 1024
ADDR = (HOST,PORT)
tcpServer =socket(AF_INET,SOCK_STREAM)
tcpServer.bind(('localhost',28888))
tcpServer.listen(5)
print("服务器已经启动  现在正在等待客户端的连接")
while True:
    tcpClient ,addr = tcpServer.accept()
    print(addr)
    while True:
        data = tcpClient.recv(BZ).decode()
        print(data)
        if not data:
            break
        data = input(">\n")
        print(data)
        tcpClient.send(data.encode())
    tcpClient.close()
tcpServer.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
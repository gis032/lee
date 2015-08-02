#encode=utf8
'''
Created on 2015年7月26日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/sixteen/cilent1.py

(
'''
from socket import *
import sys
HOST='localhost'
PORT=28888
bz = 1024
ADDR = (HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(('localhost',28888))
while True:
    data = input("请输入想说的话\n")
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(bz).decode()
    if not data:
        break
    print(data)
tcpCliSock.close()
    
    















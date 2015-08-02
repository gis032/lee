#encode=utf8
'''
Created on 2015年7月27日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/sixteen/getweb.py

(
'''
import socket
if __name__ =='__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    s.connect(('www.baidu.com',80))
    s.send("GET /index.html HTTP/1.0\r\n\r\n".encode())
    data=s.recv(4096).decode()
    print(data)
    
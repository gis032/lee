#encode=utf8
'''
Created on 2015年7月17日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/qqqq.py

(
'''
f = open("F:/python.txt", 'w',1,'gbk')
for i in range(1,10,1):
        f.write(chr(i)*20)
f.close()
print('aaa')
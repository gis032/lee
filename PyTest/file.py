#encode=utf8
'''
Created on 2015年7月16日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/file.py

(
'''
import os 
import time
import re
#如何查看内建函数
#print(dir(__builtins__))
#f1 = open(file, mode='r', buffering=_1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
def funWrite():
	f = open("F:/python.txt", 'w')
	for i in range(1,10,1):
		f.writelines(chr(i+96)*20)
	f.close()
def funcRead():
	f = open("F:/python.txt", 'U')
	lines = f.readlines()
	for line in lines:
		print(line.strip())
	f.close()	
def funcHave():
	f=open("F:/python.txt",'w',1)
	return f
def funcWriteTO():
	f = open("F:/python.txt", 'a+')
	lin =len( f.readlines())
	print(lin)
	f.seek(lin,0)
	for i in range(99,110,1):
		f.write(chr(i)*20)
		f.write(os.linesep)
	f.write(str(time.time()))
	f.close()	
def funccount():
	fi= open(r"F:\workspace\lee\PyTest\时间.txt",'r')
	sumA =0.0
	strRex = '\d*\.\d*'
	for i in fi:
		result = re.search(strRex,i)
		f1 = float(result.group())
		sumA += f1 
	print(sumA)	

if __name__=='__main__':
	funccount()
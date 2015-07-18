# encode=utf8
'''
Created on 2015年7月18日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/shurushuchu.py

(
'''
import sys
def func1(argvs):
    lis = ['+', '-', '**', '*', '/', '%']
    for li in lis:
        if li in argvs:
            if li == '+': return int(argvs[0])+int(argvs[2])
            if li == '-':return int(argvs[0])-int(argvs[2])
            if li == '**':return int(argvs[0])**int(argvs[2])
            if li == '/':return int(argvs[0])/int(argvs[2])
            if li == '%':return int(argvs[0])%int(argvs[2])
def writeF(al, li):
    f = open('sum.txt', 'a+')
    for i in li:
        f.write(i)
    f.write('\n')
    f.write(str(al));
    f.write('\n')
    f.close()
def readF():
    f = open('sum.txt', 'r+')
    for line in f:
        print(line)
    f.close()

leng = len(sys.argv)
if sys.argv[1] == 'print':
    readF()
if leng == 4:
    sumAll = func1(sys.argv[1:])     
    writeF(sumAll, sys.argv[1:])
    print('%s %s %s' % (sys.argv[1], sys.argv[2], sys.argv[3]))
    print(sumAll)









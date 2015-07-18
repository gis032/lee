#encode=utf8
'''
Created on 2015年7月16日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/Test.py

(
'''
' N！'
def funcN(n):
    if n == 1: return n
    else:
        return n*funcN(n-1)
#print(func(5))
'斐波那契数列'
def func2(n):
    if n==0 :return 0
    if n==1 :return 1
    else:
        return func2(n-1)+func2(n-2)
#十进制转换成二进制 八进制 十六进制 ASCII值
def func3(start,end):
    print("十进制\t 八进制\t十六进制\t二进制\t ASCII\t")
    print("----------"*20)
    for i in range(start ,end+1):
        print("%d\t%o\t%x\t%s\t%s"%(i,i,i,bin(i)[2:],chr(i)))



















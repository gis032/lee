#encode=utf8
'''
Created on 2015年7月19日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/eleven.py

第十一章   函数和函数式变成

python 3.3
(
'''
from time import ctime,sleep
from urllib.request import urlretrieve
from operator import  add,mul
from functools import partial
import tkinter
def func1(x,y=1):#参数的传递，针对方法的参数，我们在定义参数的时候可以给参数默认之，在我们调用参数的时候，可以指定参数的指
    print("x=%d,y=%d,x+y=%d"%(x,y,x+y))

def func2():
    print("现在是外部函数func2")
    def func22():# 在一个方法内部定义的方法只能在方法内执行，不可以在方法外执行的
        print("这个是内部韩式 func22")
    func22()
    print("方法结束")  

def tsfunc(func3):
    def warppedFunction():
        print("[%s] %s() called"%(ctime(),func3.__name__))
        #return func3()
    return warppedFunction

@tsfunc
def foo1():
    print("foo")
def func33():
    foo1()
    sleep(4)
    for i in range(2):
        sleep(1)
        foo1()


def func4():
    def func41(lines):
        for eachline in lines:#去第一个非空的行
            if not eachline.strip():
                continue
            else:
                return eachline
    def firstLast(webpag):
        f=open(webpag)
        lines = f.readlines()
        f.close()
        print(11)
        print(func41(lines))
        lines.reverse()
        print(func41(lines))
    def downL(url='http://www.baidu.com',process=firstLast):
        try:
            r = urlretrieve(url,'F:/workspace/lee/PyTest')[0]# 现在这个方法在urllib.request下
            print(r)
        except IOError as e:
            r = None
            print(e)
        if r :
            process('u'.join(r))
    downL()
            
def func5():
    def funcx(x,y,z):
        return ("x=%d y=%d z=%d sum=%d"%(x,y,z,x+x*y+y+z))
    add1 = partial(add,1)
    mul100 = partial(mul,100)
    x1 = partial(funcx,10)
    print(add1(10))
    print(mul100(10))
    print(x1(1,2))

def funcGUI():
    root = tkinter.Tk()
    Mybutton = partial(tkinter.Button,root,fg='white',bg='blue')
    b1 =Mybutton(text='Button 1')
    b2 =Mybutton(text='Button 2')
    qb =Mybutton(text='QUIT' ,bg='red',command=root.quit)
    b1.pack();
    b2.pack();
    qb.pack(fill=tkinter.X,expand=True);
    root.title("ssssss")
    root.mainloop()

def func6():#生成器
    def sss():
        yield 1
        yield '2---1'
    ss =sss()
    print(ss.__next__())


      
#func1(1,2)
#func1(2)
#func1(x=4,y=2)
#func2()
#func33()
#func4()
#func5()
#funcGUI()
func6()
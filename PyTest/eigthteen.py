#encode=utf8
'''
Created on 2015年7月24日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/eigthteen.py

#多线程编程  第十八章 python3

thread模块改名为 _thread
(
'''
from time import ctime,sleep
import _thread 
import threading
def foo1():
    print("开始foo1 %s"%(ctime()))
    sleep(4)
    print("结束foo1 %s"%(ctime()))
 
def foo2():
    print("开始foo2 %s"%(ctime()))
    sleep(2)
    print("结束foo2 %s"%(ctime()))
       
def fooMain():
    print("starting at %s" % (ctime()))        
    foo1()
    foo2()
    print("end at %s" % (ctime()))
    # 这个例子表明 是顺序执行的顺序   显示主线程进行执行，然后打印开始执行  然后执行foo1 阻塞 结束  然后在执行foo2  阻塞 执行 结束 然后在执行结束提示

def thrMain():   
    print("starting at %s" % (ctime()))        
    _thread.start_new_thread(foo1,())
    _thread.start_new_thread(foo2,())
    sleep(4)# 如果不加这句的话，主线程直接结束掉  不会管子线程是否执行完
    print("end at %s" % (ctime()))
loops=[4,2] 
def lockfoo(nloop,nsec,lock):
    print("start loop %d at %s"%(nloop,ctime()))
    sleep(nsec)
    print("end loop %d at %s"%(nloop,ctime()))
    lock.release()#释放锁
def lockMain():
    print("开始执行循环 at %s"%(ctime()))
    locks=[]
    nloop=range(len(loops)) #循环的次数
    for i in nloop:
        lock = _thread.allocate_lock()#创建所对象
        lock.acquire()#获取锁对象
        locks.append(lock)
    for i in nloop:
        _thread.start_new_thread(lockfoo,(i,loops[i],locks[i]))
    for i in nloop:
        while locks[i].locked():pass
    print("结束循环 at %s"%(ctime()))
    
def threadingfoo(nloop):
    print("start loop %d at %s"%(nloop[0],ctime()))
    print()
    sleep(nloop[1])
    print("end loop %d at %s"%(nloop[0],ctime()))
def threadingMain():#使用threading来完成线程的启动  主线程会在子线程结束后在执行
    print("开始执行循环 at %s"%(ctime()))       
    nloop=range(len(loops)) #循环的次数
    threads=[]
    for i in nloop:
        t=threading.Thread(target=threadingfoo,args=(i,loops[i]))
        threads.append(t)
    for i in nloop:
        threads[i].start()
    for i in nloop:
        threads[i].join()
    print("结束循环 at %s"%(ctime()))
class myThread(threading.Thread):
    def __init__(self,runFunc,args,name=""):
        threading.Thread.__init__(self)
        self.name=name
        self.runFunc = runFunc
        self.args = args
        print(args)
    def run(self):     
        self.runFunc(self.args)
    
def threadingClass():# 子类继承父类来完成线程
    print("开始执行循环 at %s"%(ctime()))       
    nloop=range(len(loops)) #循环的次数
    threads=[]
    for i in nloop:
        t=myThread(threadingfoo,(i,loops[i]),threadingfoo.__name__)
        threads.append(t)
    for i in nloop:
        threads[i].start()
    for i in nloop:
        threads[i].join()
    print("结束循环 at %s"%(ctime()))
    
             
if __name__ == "__main__":
#    fooMain() 
#    thrMain()
#    lockMain()
#    threadingMain()
    threadingClass()
#encode=utf8
'''
Created on 2015年7月19日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/ten.py

练习的操作是python核心编程   error and exception

这个使用的python3
(
'''
def func1():
    try:
        f = open('builtInFunction')
    except IOError as e:
        print("出现问题了，异常，读取文件爱你错误")
        print(e)
    else:#如果有异常不会执行当前的else，没有问题才会执行else，finally是无论如何都要执行的东西，出现异常以后的代码都不会执行的，出了finally
        print("aaaaaa")
    finally:
        print("出现问题来")

def func2():
    try:
        f = float([1,2])
    except (ValueError,TypeError) as e: 
        return print("类型转换错误，请重新输入正确的类型\n%s"%(e))

def func3():
    print("assert 试用")
    try:
        assert 1==0,'啦啦啦啦' # 这个就是当断言是假的时候，会报AssertionError，将信息传递到异常对象中
    except AssertionError as a:
        print(a)

def func4():
    try:
        i = 1/0
    except :
        import sys#通过sys的exc_info来查看异常的具体信息  基类  实例  栈跟踪信息
        print(sys.exc_info())      
#func1()    
#func2()    
#func3()
#func4()



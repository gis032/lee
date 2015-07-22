# encode=utf8
'''
Created on 2015年7月17日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/FileExercise.py

(
'''
from builtins import __import__
import os
import zipfile

# 过滤文件的开头是#的行
f = open(u'F:\\习题.txt', 'r+', 1, 'utf8')
def func1():
    for eachLine in f:
        if not  eachLine.startswith('#'):
            print(eachLine.strip(),)
    f.close()        
def func2():
    length = len(list(len for lines in f))
    return length         
    f.close()              
    
def func3():
    lines = f.readlines()
    num = 0;
    for line in lines:
        if num == 0:
            num = int(input("请输入显示的行数\n"))
        if num > 0:
            print(line,)
            num -= 1
                
    f.close()              

def func4():
    print(dir(__import__('os')))  

def func5():
    strA = u'D:\Python33\Lib'
    f = open("recorder", 'w', 1, 'utf8')
    
    for temp in os.listdir(strA):  # 列出文件夹下的文件  不列出文件夹
        print(os.listdir(temp))
        if os.chdir(strA + temp):
            f.write("%s 是一个目录，不是文件\n" % (temp))
        else:
            f.write("%s 是一个文件，不是目录\n" % (temp))    
    f.close()
    print("结束")
# 复制文件内容到另一个文件中去
def func6():
    f = open(u'F:\\习题.txt', 'r+', 1, 'utf8')
    f2 = open(u'习题.txt', 'w+', 1, 'utf8')
    for eachLine in f:
        f2.write(eachLine.strip())
        f2.write('\n')    

def func7():
    f = zipfile.ZipFile("hello2.zip","w")
    f.write('F:/workspace/lee/PyTest/recorder','recorder');
    f.close()
    print("ok")                      
# func1()
# func3()
# func4()
#func5()

#func6()

func7()












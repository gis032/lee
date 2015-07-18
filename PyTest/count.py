# python
'''
Created on 2015年7月12日
This file is to do some exercise
@author: Lee丶Second
'''
def func(string):
    return eval(string) #eval 将字符串当作值来计算来返回值
def func2(string):
    for op in ops:
        if op in string:
            st = string.split(op)
            print(st)
            st[0] = float(st[0])
            st[1] = float(st[1])
            if op=='+' : return st[0]+st[1]
            if op=='-' : return st[0]-st[1]
            if op=='*' : return st[0]*st[1]
            if op=='/' : return st[0]/st[1]
            if op=='**' : return st[0]**st[1]
    return "输入的数据有问题"
    return 1
ops=['+',"-","**","/","*"]
string  = input("请输入算数表达式:")
print(func(string),)
print("-----------"*5)
print(func2(string))
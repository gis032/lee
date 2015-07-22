# encode=utf8
'''
Created on 2015年7月20日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/thirteen.py

第十三章  面向对象编程

python3.5
(
'''
class class1():
    name = None  # 定义一个属性，给定初始值
    def __init__(self, name='11', age=12):  # 定义了一个方法，self相当于this，定义的时候需要使用，传参的是不需要使用
        print("class1")
        self.name = name  # 定义属性，并且赋值
        self.age = age
    def pp(self):
        print("sss")   
class class2(class1):
    def __init__(self, address='111'):
        # class1.__init__(self)#不定义这个就不会调用到class1的构造函数，就不会有在init里面定义的属性
        self.address = address
        print("class2")
        # 类是实例化的时候，如果不指明调用父类的init方法的话，不会去调用父类的初始化方法，不会递归的去寻找上级，与java不同

class p():
    def foo(self):
        print('p')
class p2():
    def bar(self):
        print("bar")
class c1(p, p2):
    pass
class c2(p, p2):
    def bar(self):
        print("c2 bar")
class xx(c1, c2):
    pass


class cc():
    __num = '1'
    def __init__(self):
        self._cc__num = 'sss'
    def pri(self):
        print(self.__num)

class baozhuang(object):
    def __init__(self, obj):
        self.__data = obj
    def get(self):
        return self.__data
    def __repr__(self):
        print("__repr__")
        return 'self.__data'
    def __str__(self):
        print("__str__")
        return str(self.__data)
    def __getattr__(self,attr):
        print("__getattr__")
        return getattr(self.__data,attr)

class slotsfunc(object):
    __slots__=('foo','bar')























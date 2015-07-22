#encode=utf8
'''
Created on 2015年7月22日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/fifteen.py

第十五章   正则表达式

python 3.5
(
'''
import re # 导入正则表达是的包

strRegx = re.compile("\.app$")
#result = re.match("foo","foo") match 匹配 从开始查找 如果没匹配 result 是None
#result = re.search("foo","dddfoo")# 在字符串中查找有这个字符串的
#re = re.match('a|b|c','a') # 多个匹配用 管道符进行连接
#re2 = re.match("[^a][\w]+","booi")
#if re2 is not None:
#    print(re2.group())

def func():
    st = ['www.baidu.com','www.alibaba.com','www.qq.com','www.oracle.org']
    strRe = '(\w){3}[\.](\w)+(\.(com|or))$'
    for i in st:
        res = re.match(strRe,i);
        if res is not None:
            print(res.group())

def func2():
    st =['01','02','03','04','05','06','07','08','09','1','10','11','12','19']
    strRe = '(0?[1-9])$|(1[0-2])'
    for i in st:
        res = re.match(strRe,i);
        if res is not None:
            print(res.group())
def func3():
    st=['800-555-1212','555-1212','(800)555-1212','999-555-6666']
    strRe = '((\(8\d{2}\))|(8\d{2}-))?\d{3}-\d{4}'
    for i in st:
        res = re.match(strRe,i);
        if res is not None:
            print(res.group())
if __name__ == "__main__":  
    func3()













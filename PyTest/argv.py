#encode=utf8
'''
Created on 2015年7月18日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/PyTest/argv.py

(
'''
#输入参数  然后在sys.argv中保存
# argc 就是len(sys.argv)  argv[0]是文件名 1 之后是参数 类似于shell的$0 代表是执行文件的名称 $1--$9代表的是参数
import sys
for i in range(0,len(sys.argv)):
    print(sys.argv[i])
print('共%d个参数'%(len(sys.argv)))
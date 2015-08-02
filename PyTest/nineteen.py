#encode=utf8
'''
Created on 2015年7月24日

@author:  李文强   liwenqiang

@Email ：liwenqiang2410@gmail.com

F:/workspace/lee/PyTest/nineteen.py

图形化界面      GUI   python3
(
'''
import tkinter
from tkinter.constants import *
def func1():
    root = tkinter.Tk()
    tkinter.colorchooser='black'
    bu = tkinter.Button(fg="red", bg="blue")
    bu["text"] = "Hello World\n(click me)"
    bu.pack(side="bottom")
    tkinter.mainloop()
def func2():
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    label = tkinter.Label(frame, text="Hello, World")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()    
if __name__ =='__main__':
    func1()
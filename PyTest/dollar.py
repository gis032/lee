# python
'''
Created on 2015年7月12日
This file is to do some exercise
@author: Lee丶Second
'''
def func(money):
    print("当前输入的金额是%f"%(money))
    m1 = money*100
    m25 = int(m1/25) # 可以有多少个25
    m1 = m1-25*m25
    m10 = int(m1/10)
    m1 = m1 - m10 *10
    m5 = int(m1/5)
    m1 = int(m1-m5*5)
    return [m25,m10,m5,m1]
money = float(input("请输入进入money:"))
print(func(money))
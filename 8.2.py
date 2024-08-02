# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:58:31 2024

@author: lys
"""
number=[]

n=input("請輸入次數:")

for i in range(100):
    if i==0:
        number.append(1) 
        print(list(number))
    elif i==1:
        a=1
        number=[1,a]
        
    else:
        100>i>=2
        temp1=number.pop(0)
        temp2=number.pop(1)
        b=int(temp1)+int(temp2)
        if i==b:
            number.append(temp1,temp2,a)
        else:
            i!=b
            continue
    print(list(number))   




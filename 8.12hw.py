# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 13:28:44 2024

@author: tat95
"""
number=[]
while len(number)!=3:
    a=int(input("輸入3個數字"))
    if a>=0:
        number.append(a)
        number.sort()
    

    print(number)
    
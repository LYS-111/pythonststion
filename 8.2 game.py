# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:04:20 2024

@author: lys
"""

import random

card = []

for i in range(4):
    for n in range(1,14):
        if n > 10:
            card.append(0.5)
        else:    
            card.append(n)
        
print('張數：',len(card))
#print(card)        
print()
# 洗牌


for i in range(300):
    start = random.randint(0,51)
    end = random.randint(0,51)
    
    card[start],card[end] = card[end],card[start]
    

print(card)    

mymoney=100
minvalue=10
maxvalue=100


while True:
    q = input("是否要玩10點半(yy/n):")
    print("目前存款:",mymoney)
    
    if q == 'n':
       break
    elif q == 'y':
        mymomey<=0:
        print("餘額不足,遊戲結束")
        break
        
    z=int(input("賭注為:(最少為10,最多為100):"))
    if z>=10 and z<=100:    
        mymoney=mymoney-z
        print("剩餘存款:",mymoney)
    elif z<=0:
        print("賭注太小")
    
    
    com = []
    player = []
    
    com.append(card.pop())
    player.append(card.pop())
    
    #玩家的
    count=1
    while True:
        print('玩家目前點數：',sum(player))
        if sum(player)>=10.5 or count==5:
            break
        
        q = input("是否要補牌？(y/n):")
        if q == 'n':
            break
        
        number = card.pop()
        print("點數：",number)
        player.append(number)
        count += 1
        
    if sum(player) > 10.5:
        print("玩家爆了！！！")
    elif sum(player) == 10.5 or count == 5:
        print("玩家Win")
    else:
        
        while True:
            print('莊家目前點數：',sum(com))
            
            if sum(com)>=10.5 or sum(com) >= sum(player) :
                break
                    
            number = card.pop()
            print("點數：",number)
            com.append(number)        

        #判斷的程式???

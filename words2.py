# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 17:48:55 2025

@author: cstb31
"""

def funcwords(a):
    if a==0:
        return"ZERO"
    elif a==1:
        return"ONE"
    elif a==2:
        return"TWO"
    elif a==3:
        return"THREE"
    elif a==4:
        return"FOUR"
    elif a==5:
        return"FIVE"
    elif a==6:
        return"SIX"
    elif a==7:
        return"SEVEN"
    elif a==8:
        return"EIGHT"
    elif a==9:
        return"NINE"
    else:
        return"NONE"      
a=int(input("Enter a Number:"))                             
b=int(input("Enter a Number:"))

if a>b:
    c=a//10;
    d=a%10
    print("The Greatest Nuimber is",a)
else:
    c=b//10;
    d=b%10
    print("The Greatest Nuimber is",b)
    
r1=funcwords(c)
r2=funcwords(d)
print(r1,"",r2)










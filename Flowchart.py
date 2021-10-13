# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 12:53:36 2021

@author: 喵先生
"""
#Compare
def Print_values():
    print("Please enter 3 numbers: ")
    print("-" * 40)
    a = int(input("Please enter the first number called a: "))
    b = int(input("Please enter the second number called b: "))
    c = int(input("Please enter the third number called c: "))
    if a > b:
        if b > c:
            print("The order is a:",a ,", b:",b, ", c:" ,c )
        elif a > c:
            print("The order is a:", a , ", c:", c ,", b:",b )
        else:
            print("The order is c:", c ,", a:", a , ", b:", b )
    elif b > c:
        print("null")
    else:
        print("The order is c:", c , ", b:", b , ", a:", a )
Print_values()

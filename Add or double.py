# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:45:32 2021

@author: 喵先生
"""

#Add or double
import random
import numpy as np

def Least_moves():
    x = random.randint(1, 101)
    print("The initial number is x: ", x)
    print("*" * 40)
    print(x)
    i = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            i += 1
            print(int(x))
        else:
            x = x - 1
            i += 1
            print(int(x))
            x = x / 2
            print(int(x))
            i += 1
    print("*" * 40)
    print(i, "steps in total." )
Least_moves()


    
    
    
    
    
    
    
    
    
    
    
    
    

    
        
 
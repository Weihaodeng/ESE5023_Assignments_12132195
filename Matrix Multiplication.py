# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:42:23 2021

@author: 喵先生
"""
#Create 2 matrices
import random
import numpy as np
#M1 (5 * 10)
M1 = np.random.randint(0, 51, (5, 10))
print(M1)
#M2 (10 * 5)
M2 = np.random.randint(0, 51, (10, 5))
print(M2)


import random
import numpy as np
M1 = np.random.randint(0, 51, (5, 10))
print(M1)
M2 = np.random.randint(0, 51, (10, 5))
print(M2)
def Matrix_multip():
    Answer = [[0] * len(M2[0]) for i in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2)):
            for k in range(len(M2[0])):
                Answer[i][k] += M1[i][j] * M2[j][k]
    return(Answer)
Matrix_multip()


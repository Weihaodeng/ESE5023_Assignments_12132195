# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:21:23 2021

@author: 喵先生
"""
#在每一行最后位置补0
def Pascal_triangle():
    Pas = [[1]]
    k = int(input("Please enter the row's value k: "))
    for i in range(1, k):
        temp = Pas[i-1] + [(0)]
        result = [1]
        for j in range(len(temp) - 1):
            result.append(temp[j] + temp[j+1])
        Pas.append(result)
    print(Pas[-1])                      #输出最后一行即第k行结果
Pascal_triangle()
    



    
    
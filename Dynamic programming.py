# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 17:02:53 2021

@author: 喵先生
"""
#The first question   
import random
import numpy as np

result = []
aim = np.random.randint(1, 101)                         #必须使用np，否则type不同
def Find_expression(aim: int, b):
    operator = ["+", "-", ""]
    def make_it(b):
        if len(b) == 1:                                 #b: "123456789"
            return [b]
        else:
            return [b[0] + op + x for x in make_it(b[1:]) for op in operator] 
    return [ Re + "=" + str(aim) for Re in make_it(b) if eval(Re) == aim] 
      
if __name__ == "__main__":                              #运行全体       
    results = Find_expression(aim, "123456789")
    print("Finished!!!")
    print("Aim is: ", aim)
    print(results)
    
#The second question
Total_list = []
for aim in range(1, 101):                               #范围内调用函数
    Goal = Find_expression(aim, "123456789")
    Total_list.append(Goal)
print(Total_list)
  
    
    




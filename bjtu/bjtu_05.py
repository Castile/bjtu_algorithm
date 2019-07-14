# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:17:54 2019

@author: ZHLAS
"""


class magician():
    def __init__(self, low_score, mid_score, high_score):
        self.score1 = low_score
        self.score2 = mid_score
        self.score3 = high_score

class test():
    def __init__(self, n, cv):
        
        self.num = n
        self.cv = cv 
T = int(input())
Test = list() # T组测试用例
for i in range(T): # T个测试用例
    cv = list() #存储简历
    n = int(input()) # 简历的份数
    for j in range(n): # 输入简历
        s = input()
        score = []
        if s != "":
            for d in s.split():
                score.append(int(d)) # 存储每门课的成绩
        cv.append(score)
    t = test(n, cv)
    Test.append(t)   
for i in range(T):
    a = 0 # 三种人的数量
    b = 0
    c = 0
    for k in range(Test[i].num):
        if Test[i].cv[k][-1] >= 60:
            a+=1
            b+=1
            c+=1
            
        elif Test[i].cv[k][-2] >=60:
            b+=1
            a+=1
            
        elif Test[i].cv[k][-3] >=60:
            a+=1
    print("Case #%d: %d %d %d" % (i+1, a, b, c))
        
        
        
        
        









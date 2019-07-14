# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:17:54 2019


魔法
成绩: 5 / 折扣: 0.8
题面描述
魔法部急缺一批魔法师，于是他们急急忙忙新招聘了一批魔法师，应聘魔法师在他们上交的简历里写了各自的学历。学历仅包括初级魔法、中级魔法和高级魔法三门课程的成绩情况，用百分制表达。如果一位魔法师在某门课程上及格 (>=60 分 ) 的话，他就能得到相应的职称并担任对应的职业。当然，有高级职称的人可以担任低级职业。由于交上来的简历太多了，魔法部的负责人找到了你，想让你帮忙计算，能担任初级、中级、高级魔法师的人分别有多少人 ?

输入数据
输入数据第一行为一个正整数 T ，表示测试数据的组数。 接下来是 T 组测试数据，每组测试数据的第一行为一个整数 n ，表示简历份数，随后的 n 行中，每行以低级、中级、高级的顺序表示三门课的成绩（ 1≤T≤100 ， 1≤n≤1000 ， 0≤ 成绩 ≤100 ）。

输出数据
对于每一组输入数据，输出一行形如 ”Case #id: a b c” 的结果 , 表示第 id 组数据结果是 a,b,c ， id 从 1 开始， a,b,c 表示三种人的数量。

样例输入
2
3
12 23 99
66 66 77
99 88 23
2
100 100 100
100 100 100

样例输出
Case #1: 3 3 2
Case #2: 2 2 2

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
        
        
        
        
        









# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:12:04 2019


连续数的和
成绩: 5 / 折扣: 0.8
题面描述
对于一个给定的正整数 n ，请你找出一共有多少种方式使 n 表示为若干个连续正整数的和，要求至少包括两个正整数。如 n=15 时，可以有 3 种方式：（ 1+2+3+4+5 ），（ 4+5+6 ），（ 7+8 ）。

输入数据
输入数据第一行为一个正整数 T ，表示测试数据的组数。 随后的 T 行中，每行包括一组测试数据，为一个整数 n（1≤T≤1000,n≤10^9）。

输出数据
对每一组输入数据，输出一行结果 ”Case #id: M” ，表示第 id 组数据的结果是 M ， id 从 1 开始。

样例输入
2
3
15

样例输出
Case #1: 1
Case #2: 3

@author: ZHLAS
"""

#for i in range(T):
#    #d = data[i]
#    a = 1
#    b = a+1
#    count = 0
#    summ = a + b
#    m = data[i]/2 + 1
#    while a <= b and b <= m:
#        if summ == data[i]:
#            count = count + 1 # 计数
#            # 打印结果: 从a连续加到b
##            print("Case #%d: n = %d :" % (i + 1, d))
##            for k in range(a, b+1):
##                if k != b:
##                    print("%d +" % k, end = ' ')
##                else:
##                    print("%d" % k)      
#            summ = summ - a
#            a = a + 1           
#        elif summ < data[i]: # 小了
#            b = b + 1
#            summ = summ + b
#        else: # 大了
#            summ = summ - a
#            a = a + 1 
#    print("Case #%d: %d" % (i + 1, count))

#for i in range(T):
#    count = 0
#    if data[i] == 3:
#        print("Case #%d: %d" % (i + 1, 1))
#        continue
#    for k in range(1, int(data[i] / 2) + 1):
#        if 2*data[i] % k == 0:
#            if ((int(2*data[i] / k)) - k + 1) % 2 == 0  and int(2*data[i] / k) - k + 1 > 0: 
#                count = count + 1
#    print("Case #%d: %d" % (i + 1, count-1))
def compute(n):
    result = 0
    k = 1
    while k * (k + 1) <= 2 * n:
        if ((n - k * (k + 1) / 2) % k == 0):
            result += 1
        k += 1
    return result-1        
T = int(input())
data = list()
for i in range(T):
    a = int(input())
    data.append(a)    
for i in range(T):
    count = compute(data[i])
    print("Case #%d: %d" % (i + 1, count))
    

        
    
    
        
        
        
    
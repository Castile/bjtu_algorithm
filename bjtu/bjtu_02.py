# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:14:13 2019
北交 02


@author: ZHLAS
"""


#T = int(input()) # T 组测试用例
#data = list()
#p = [0]*T
#n = [0]*T
#for i in range(T):
#    s = input()
#    inp = []
#    if s != "":
#        for a in s.split():
#            inp.append(int(a))
#    n[i],p[i] = inp
#    d = [x for x in range(1,n[i]+1)] # 生成这个测试用例的数据
#    data.append(d)
#for i in range(T):
#    count = 1
#    data[i][0] = None 
#    
#    j = p[i]
#    index = j % n[i]
#    while data[i][index] != None:
#        count = count+1
#        data[i][index] = None
#        j = j + p[i]
#        index = j % n[i]
#    print("Case #%d: %d" % (i+1, count))
    
# 最大公约数
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)   
def count(N, M):
    g = gcd(N, M)
    if g == 1:
        return N
    else:
        N = N/g
        return N   
T = int(input()) # T 组测试用例
p = [0]*T
n = [0]*T
for i in range(T):
    s = input()
    inp = []
    if s != "":
        for a in s.split():
            inp.append(int(a))
    n[i],p[i] = inp
for i in range(T):
    c = count(n[i], p[i])
    print("Case #%d: %d" % (i+1, c))
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
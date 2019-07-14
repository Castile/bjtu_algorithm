# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:37:33 2019
互素

题面描述
小明很喜欢学数学，并且喜欢做一些奇怪的题，这天他想知道对于给定的 N ，有多少个 M 满足“ M<=N, gcd(N,M)==1, M 是偶数”。请你编写程序帮助小明解决这个问题。

输入数据
输入数据第一行为一个正整数 T ，表示测试数据的组数。 接下来的 T 组测试数据中， 每组测试数据为一行，包含一个整数 N （1≤T≤100， 1≤N≤10000 ）。

输出数据
对于每一组输入数据，在单独的一行中输出 ”Case #id: M”, 表示第 id 组数据结果是 M ， id 从 1 开始；

样例输入
4
1
2
11
23

样例输出
Case #1: 0
Case #2: 0
Case #3: 5
Case #4: 11

Hint:
gcd(a,b)==1 表示 a 与 b 的最大公约数为 1 ，即 a 与 b 互素。


@author: ZHLAS
"""
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b) 
T = int(input()) # T 组测试样例
data = list()
for i in range(T):
    a = int(input())
    data.append(a)
for i in range(T):
    count = 0
    M = [x for x in range(1, data[i] + 1) if x % 2 == 0]
    for x in M:
        flag = gcd(data[i], x)
        if flag == 1:
            count = count + 1
    print("Case #%d: %d" % (i+1, count))
        
        
    


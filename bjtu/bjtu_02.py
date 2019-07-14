# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 21:14:13 2019
北交 02

绕圆圈
成绩: 5 / 折扣: 0.8
题面描述
小明报名参加了趣味运动会，运动会游戏规则如下：在一个环形跑道上，等距离放置着 N 个小球，小球按照顺时针方向从起点开始依次编号为 1 到 N ，在最短时间内取走放在跑道上尽可能多小球的选手获胜。举办方要求每个选手只能按照顺时针方向，跳过 M-1 个号码取后走下一个小球。如当 N=5 、 M=3 时，小明能够取走所有的小球，取走的顺序依次为 1->4->2->5->3 。当 N=6 、 M=2 时，小明只能取走 3 个小球 1->3->5 。小明想知道在一场比赛中他最多能取走多少小球，当然，小明是知道怎么做的，但是他忙着补作业，所以这个简单的问题就交 (shuai guo) 给你了。

输入数据
输入数据的第一行为一个整数 T ，表示有 T 组测试样例。每组样例为单独的一行，包括两个整数 N 和 M 。

输出数据
对每一组输入数据，输出一行结果 ”Case #id: M” ，表示第 id 组数据的结果是 M ， id 从 1 开始。

样例输入
3
5 3
6 2
10 6

样例输出
Case #1: 5
Case #2: 3
Case #3: 5


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
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 16:49
# @Author  : 一叶知秋
# @File    : 合唱队.py
# @Software: PyCharm
"""
题目描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：

N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，   则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

请注意处理多组输入输出！


输入描述:
整数N

输出描述:
最少需要几位同学出列

示例1
输入
复制
8
186 186 150 200 160 130 197 200
输出
复制
4
"""


# 链接：https: // www.nowcoder.com / questionTerminal / 6
# d9d69e3898f45169a441632b325c7b4?f = discussion
# 来源：牛客网


# dp的二分优化，tail记录每个长度子序列的最后一个元素
def maxup(L, N):
    up = []
    tail, res = [0] * N, 0
    for num in L:
        i, j = 0, res
        while i < j:
            mid = (i + j) // 2
            if tail[mid] < num:
                i = mid + 1
            else:
                j = mid
        tail[i] = num
        up.append(j)
        if j == res: res += 1
    return up


def main():
    while True:
        try:
            N = int(input())
            L = [int(c) for c in input().strip().split()]
            up = maxup(L, N)
            down = maxup(L[::-1], N)
            down = down[::-1]
            for i in range(N):
                up[i] += down[i]
            res = N - max(up) - 1
            print(res)
        except:
            break


if __name__ == '__main__':
    main()

"""
链接：https://www.nowcoder.com/questionTerminal/6d9d69e3898f45169a441632b325c7b4?f=discussion
来源：牛客网
import bisect

def deal(l,res):
    b    = [float('inf')]*len(l)
    b[0] = l[0]
    res  = res+[1]
    for i in range(1,len(l)):
        pos =bisect.bisect_left(b,l[i])
        b[pos]=l[i]
        res += [pos+1]
    return res
 
def main(n,s):
    n = int(n)
    s = list(map(int,s.split()))
    dp1, dp2=[], []
    dp1 =deal(s,dp1)
    dp2 =deal(s[::-1],dp2)[::-1]
    return n-max(map(sum,zip(dp1,dp2)))+1
 
while 1:
    try:
        print(main(input(),input()))
    except:
        exit()
"""
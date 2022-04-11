#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 22:23
# @Author  : 一叶知秋
# @File    : 质数因子.py
# @Software: PyCharm
"""
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）
最后一个数后面也要有空格
详细描述：
函数接口说明：
public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：
String

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
复制
180
输出
复制
2 2 3 3 5
"""


# 方法一
def method():
    a, res = int(input()), []
    for i in range(2, a // 2 + 1):  # a除以比a/2大的数，结果是1点几，肯定不是一个因子。a//2表示取整数，range函数不会到a//2，所以要在后面加上1
        while a % i == 0:
            a /= i
            res.append(i)
    print(" ".join(map(str, res)) + " " if res else f'{str(a)} ')


# 方法二
def method2():
    while True:
        try:
            a = int(input())
            b = []
            # 从2开始寻找质数因子
            for i in range(2, a // 2 + 1):
                while a % i == 0:
                    a /= i
                    b.append(i)
            if not b:
                b.append(a)
            for j in b:
                print(j, end=" ")
        except:
            break


def main():
    method()
    # method2()


if __name__ == '__main__':
    main()

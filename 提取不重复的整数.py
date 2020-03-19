#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 10:47
# @Author  : 一叶知秋
# @File    : 提取不重复的整数.py
# @Software: PyCharm
"""
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
复制
9876673
输出
复制
37689
"""


def reverse_set(num):
    result = []
    for i in str(num)[::-1]:
        if i not in result:
            result.append(i)
    return int("".join(result))


def reverse_set2(num):
    result = ""
    for i in str(num)[::-1]:
        if i not in result:
            result += i
    return int(result)


def main():
    n = int(input())
    res = reverse_set(n)
    print(res)


if __name__ == '__main__':
    main()

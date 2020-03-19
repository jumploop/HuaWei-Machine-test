#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:48
# @Author  : 一叶知秋
# @File    : 字串的连接最长路径查找.py
# @Software: PyCharm
"""
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。
示例1
输入
复制
9
cap
to
cat
card
two
too
up
boat
boot
输出
复制
boat
boot
cap
card
cat
to
too
two
up
"""


def main():
    n = int(input())
    result = []
    while n > 0:
        result.append(input())
        n -= 1
    for i in sorted(result):
        print(i)

if __name__ == '__main__':
    main()

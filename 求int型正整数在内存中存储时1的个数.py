#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:57
# @Author  : 一叶知秋
# @File    : 求int型正整数在内存中存储时1的个数.py
# @Software: PyCharm
"""
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
复制
5
输出
复制
2
"""


def main():
    print(bin(int(input())).count("1"))


if __name__ == '__main__':
    main()

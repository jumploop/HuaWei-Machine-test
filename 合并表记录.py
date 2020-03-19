#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 10:16
# @Author  : 一叶知秋
# @File    : 合并表记录.py
# @Software: PyCharm
"""
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
复制
4
0 1
0 2
1 2
3 4
输出
复制
0 3
1 2
3 4

"""


def main():
    n = int(input())
    result = {}
    while n > 0:
        key, value = input().split()
        key = int(key)
        if key not in result:
            result[key] = int(value)
        else:
            result[key] += int(value)
        n -= 1
    for k, v in sorted(result.items(), key=lambda x: x[0]):
        print(k, v, sep=" ")


if __name__ == '__main__':
    main()

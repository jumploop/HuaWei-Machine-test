#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 11:06
# @Author  : 一叶知秋
# @File    : 字符个数统计.py
# @Software: PyCharm
"""
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
复制
abc
输出
复制
3
"""


def main():
    input_string = input()
    length = len({i for i in input_string if ord(i) in range(128)})
    print(length)

if __name__ == '__main__':
    main()

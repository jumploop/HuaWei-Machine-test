#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 21:54
# @Author  : 一叶知秋
# @File    : 字符串分隔.py
# @Software: PyCharm
"""
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
复制
abc
123456789
输出
复制
abc00000
12345678
90000000
"""


def print_string(line):
    if len(line) <= 8:
        print(line + "0" * (8 - len(line)))
    else:
        print(line[:8])
        print_string(line[8:])


def main():
    str_list = [input() for _ in range(2)]
    for line in str_list:
        print_string(line)


if __name__ == '__main__':
    main()

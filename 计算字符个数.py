#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 17:19
# @Author  : 一叶知秋
# @File    : 计算字符个数.py
# @Software: PyCharm
"""
题目描述
写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。
输入描述:
第一行输入一个有字母和数字以及空格组成的字符串，第二行输入一个字符。
输出描述:
输出输入字符串中含有该字符的个数。

示例1
输入
复制
ABCDEF
A
输出
复制
1
"""
from collections import Counter


def count_char_num(string, char):
    """
    计算字符串中包含字符的个数
    :param string: 输入的字符串
    :param char: 一个字符
    :return:包含的字符个数
    """
    if char.isupper():
        string = string.upper()
    else:
        string = string.lower()
    counter = Counter(string)
    return counter[char]


def main():
    input_string = input()
    input_char = input()
    num = count_char_num(input_string, input_char)
    print(num)


if __name__ == '__main__':
    main()

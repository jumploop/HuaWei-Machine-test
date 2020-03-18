#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 17:04
# @Author  : 一叶知秋
# @File    : 字符串最后一个单词的长度.py
# @Software: PyCharm
"""
计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

示例1
输入
hello world
输出
5
"""


def cal_string_last_word_length(line):
    """
    计算字符串最后一个单词长度
    :param line: 输入字符串
    :return: 最后一个单词长度
    """
    words = line.split()
    return len(words[-1])


def main():
    str_line = input()
    lens = cal_string_last_word_length(str_line)
    print(lens)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 16:24
# @Author  : 一叶知秋
# @File    : 删除字符串中出现次数最少的字符.py
# @Software: PyCharm
"""
题目描述
实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
注意每个输入文件有多组输入，即多个字符串用回车隔开
输入描述:
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述:
删除字符串中出现次数最少的字符后的字符串。

示例1
输入
复制
abcdd
输出
复制
dd
"""

from collections import Counter


def main():
    while True:
        try:
            string = input()
            count = Counter(string)
            m = min(count.values())
            for i in count:
                if count[i] == m:
                    string = string.replace(i, "")
            print(string)
        except:
            break


if __name__ == '__main__':
    main()

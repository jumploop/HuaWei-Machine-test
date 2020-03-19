#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 22:14
# @Author  : 一叶知秋
# @File    : 进制转换.py
# @Software: PyCharm
"""

写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。（多组同时输入 ）

输入描述:
输入一个十六进制的数值字符串。

输出描述:
输出该数值的十进制字符串。

示例1
输入
0xA
输出
10
"""


def main():
    while True:
        try:
            print(int(input(), 16))
        except:
            break


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 9:57
# @Author  : 一叶知秋
# @File    : 取近似值.py
# @Software: PyCharm
"""
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
复制
5.5
输出
复制
6
"""
from math import ceil, floor


def round_number(num):
    num_list = str(num).split(".")
    return ceil(num) if int(num_list[1][0]) >= 5 else floor(num)


def main():
    float_num = float(input())
    result = round_number(float_num)
    print(result)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 13:16
# @Author  : 一叶知秋
# @File    : 简单错误记录.py
# @Software: PyCharm
"""
题目描述
开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。

处理：

1、 记录最多8条错误记录，循环记录（或者说最后只输出最后出现的八条错误记录），对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；


2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；


3、 输入的文件可能带路径，记录文件名称不能带路径。


输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。

输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

示例1
输入
复制
E:\V1R2\product\fpgadrive.c   1325
输出
复制
fpgadrive.c 1325 1
"""

import sys


def method():
    errors = {}
    files = []
    for line in sys.stdin:
        vec = line.strip().split()
        file = vec[0].split("\\")[-1]
        filename = file if len(file) < 16 else file[-16:]
        line_no = vec[1]
        mark = f"{filename}_{line_no}"
        if mark not in files:
            files.append(mark)
            errors[mark] = 1
        else:
            errors[mark] += 1

    for mark in files[-8:]:
        vec = mark.split("_")
        file = vec[0]
        print(f"{file} {vec[1]} {errors[mark]}")


def method2():
    error = {}
    files = []
    while True:
        try:
            file_num = input().strip().split('\\')[-1].split()
            filename = file_num[0] if len(file_num[0]) < 16 else file_num[0][-16:]
            line_no = file_num[1]
            record = ' '.join((filename, line_no))
            if record not in error:
                error[record] = 1
                files.append(record)
            else:
                error[record] += 1
        except:
            break
    for i in files[-8:]:
        print(' '.join(i.split()), error[i])


def main():
    method()
    # method2()


if __name__ == '__main__':
    main()

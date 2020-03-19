#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 17:34
# @Author  : 一叶知秋
# @File    : 坐标移动.py
# @Software: PyCharm
"""
题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

注意请处理多组输入输出

输入描述:
一行字符串

输出描述:
最终坐标，以,分隔

示例1
输入
复制
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出
复制
10,-10
"""


def main():
    while True:
        try:
            string = input()
            coord = [0, 0]
            str_list = string.split(";")  # 字符串分割存入列表
            for i in str_list:
                if i.startswith("A") and len(i) <= 3 and i[1:].isdigit():  # 数字（两位以内）
                    coord[0] += -int(i[1:])
                elif i.startswith("D") and len(i) <= 3 and i[1:].isdigit():
                    coord[0] += int(i[1:])
                elif i.startswith("W") and len(i) <= 3 and i[1:].isdigit():
                    coord[1] += int(i[1:])
                elif i.startswith("S") and len(i) <= 3 and i[1:].isdigit():
                    coord[1] += -int(i[1:])
                else:
                    continue
            print("{0},{1}".format(coord[0], coord[1]))
        except:
            break


if __name__ == '__main__':
    main()

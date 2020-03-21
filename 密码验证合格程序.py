#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 15:55
# @Author  : 一叶知秋
# @File    : 密码验证合格程序.py
# @Software: PyCharm
"""
题目描述
密码要求:

1.长度超过8位

2.包括大小写字母.数字.其它符号,以上四种至少三种

3.不能有相同长度超2的子串重复

说明:长度超过2的子串

输入描述:
一组或多组长度超过2的子符串。每组占一行

输出描述:
如果符合要求输出：OK，否则输出NG

示例1
输入
复制
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000
输出
复制
OK
NG
NG
OK
"""
from re import findall


def check_passwd(passwd):
    repetition = findall(r'(.{3,}).*\1', passwd)
    b1, b2, b3, b4 = findall(r"\d", passwd), findall(r"[a-z]", passwd), findall(r"[A-Z]", passwd), findall(
        r"[^0-9a-zA-Z]", passwd)
    if len(passwd) > 8 and [b1, b2, b3, b4].count([]) <= 1 and not repetition:
        print("OK")
    else:
        print("NG")


def main():
    try:
        while True:
            pw = input().strip()
            check_passwd(pw)
    except:
        pass

if __name__ == '__main__':
    main()

"""
链接：https://www.nowcoder.com/questionTerminal/184edec193864f0985ad2684fbc86841?f=discussion
来源：牛客网

import re
try:
    while 1: 
        s = input()
        a = re.findall(r'(.{3,}).*\1', s)
        b1 = re.findall(r'\d', s)
        b2 = re.findall(r'[A-Z]', s)
        b3 = re.findall(r'[a-z]', s)
        b4 = re.findall(r'[^0-9A-Za-z]', s)
 
        print 'OK' if ([b1, b2, b3, b4].count([]) <= 1 and a == [] and len(s) > 8) else 'NG'
except:
    pass
"""

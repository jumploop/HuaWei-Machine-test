#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 16:41
# @Author  : 一叶知秋
# @File    : 句子逆序.py
# @Software: PyCharm
"""
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符


接口说明

/**
 * 反转句子
 *
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);







输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1
输入
复制
I am a boy
输出
复制
boy a am I
"""


def reverse(statement):
    words = statement.split()
    return " ".join(words[::-1])


def main():
    statement = input()
    result = reverse(statement)
    print(result)


if __name__ == '__main__':
    main()

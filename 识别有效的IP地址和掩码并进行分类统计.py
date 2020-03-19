#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/19 18:32
# @Author  : 一叶知秋
# @File    : 识别有效的IP地址和掩码并进行分类统计.py
# @Software: PyCharm
"""
题目描述
请解析IP地址和对应的掩码，进行分类识别。要求按照A/B/C/D/E类地址归类，不合法的地址和掩码单独归类。

所有的IP地址划分为 A,B,C,D,E五类

A类地址1.0.0.0~126.255.255.255;

B类地址128.0.0.0~191.255.255.255;

C类地址192.0.0.0~223.255.255.255;

D类地址224.0.0.0~239.255.255.255；

E类地址240.0.0.0~255.255.255.255


私网IP范围是：

10.0.0.0～10.255.255.255

172.16.0.0～172.31.255.255

192.168.0.0～192.168.255.255


子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）
注意二进制下全是1或者全是0均为非法

注意：
1. 类似于【0.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时可以忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的

输入描述:
多行字符串。每行一个IP地址和掩码，用~隔开。

输出描述:
统计A、B、C、D、E、错误IP地址或错误掩码、私有IP的个数，之间以空格隔开。

示例1
输入
复制
10.70.44.68~255.254.255.0
1.0.0.1~255.0.0.0
192.168.0.2~255.255.255.0
19..0.~255.255.255.0
输出
复制
1 0 1 0 0 2 1
"""
import re


def isLegalIP(IP):
    if not IP or IP == "":
        return False

    pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    match = pattern.match(IP)
    if not match:
        return False

    nums = IP.split(".")
    for num in nums:
        n = int(num)
        if n < 0 or n > 255:
            return False
    return True


def CatagoryIP(IP):
    if not IP or IP == "":
        return False
    nums = IP.split(".")
    # A
    if 126 >= int(nums[0]) >= 1:
        return "A"
    # B
    if 191 >= int(nums[0]) >= 128:
        return "B"
    # C
    if 223 >= int(nums[0]) >= 192:
        return "C"
    # D
    if 239 >= int(nums[0]) >= 224:
        return "D"
    # E
    if 255 >= int(nums[0]) >= 240:
        return "E"

    return False


def isPrivateIP(IP):
    if not IP or IP == "":
        return False

    nums = IP.split(".")
    if int(nums[0]) == 10:
        return True
    if int(nums[0]) == 172:
        if 31 >= int(nums[1]) >= 16:
            return True
    if int(nums[0]) == 192 and int(nums[1]) == 168:
        return True

    return False


def isLegalMaskCode(Mask):
    if not Mask or Mask == "":
        return False
    if not isLegalIP(Mask):
        return False

    binaryMask = "".join(map(lambda x: "{0:08b}".format(int(x)), Mask.split(".")))
    indexOfFirstZero = binaryMask.find("0")
    indexOfLastOne = binaryMask.rfind("1")
    if indexOfLastOne > indexOfFirstZero:
        return False
    return True


def main():
    try:
        A, B, C, D, E, Err, P = [0, 0, 0, 0, 0, 0, 0]
        while True:
            s = input()
            IP, Mask = s.split("~")
            if not isLegalIP(IP) or not isLegalMaskCode(Mask):
                Err += 1
            else:
                if isPrivateIP(IP):
                    P += 1
                cat = CatagoryIP(IP)
                if cat == "A":
                    A += 1
                if cat == "B":
                    B += 1
                if cat == "C":
                    C += 1
                if cat == "D":
                    D += 1
                if cat == "E":
                    E += 1
    except:
        print(A, B, C, D, E, Err, P)
        pass


if __name__ == '__main__':
    main()

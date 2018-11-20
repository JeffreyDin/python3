#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 15:29
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test-while.py
# @Software: PyCharm


# 斐波纳契数列,编程第一步。
# b=1,a:1 b:1.  b=1,a:1 b:2.   b=2,a:2 b:3.   b=3,a:3 b:5.   b=5,a:5 b:8.  b=8,a:8 b:13.  b=13
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b


# 计算1到100的总和
n = 100
summer = 0
counter = 1
while counter <= n:
    summer = summer + counter
    counter += 1
print("1到%d之和为：%d" % (n, summer))


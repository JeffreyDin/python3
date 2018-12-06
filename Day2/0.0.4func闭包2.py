#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 14:16
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.11test2.py
# @Software: PyCharm


# 使用闭包实现计数器
# def counter():
#     cnt = [0]
#
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#     return add_one
#
#
# num1 = counter()
# print(num1())


# 俩个计数器
def counter(a=0):
    cnt = [a]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num5 = counter(5)
num10 = counter(10)
print(num5())
print(num5())
print(num10())
print(num10())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 22:03
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 5.0.0exception_handing.py
# @Software: PyCharm

# NameError：变量未定义
# i = j

# SyntaxError：语法错误
# print())

# IndexError: 索引错误之超过索引范围
# a = '123'
# print(a[3])

# KeyError:对应值错误
# d = {'a': 1, 'b': 2}
# print(d['c'])

# ValueError: invalid literal for int() with base 10: 'abc'
# 值误差
# year = int(input('input year: '))

# 捕获异常之ValueError
# try:
#     year = int(input('input year: '))
# except ValueError:
#     print("年份要输入数字！")

a = [1, 2, 3]
a.append(4)
print(a)


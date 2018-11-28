#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 17:03
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.1func迭代器和生成器.py
# @Software: PyCharm

# 函数的迭代器和生成器
# list1 = [1, 2, 3, 4]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))  # except

# for i in range(10, 20, 0.5):
#     print(i)

# 函数的生成器，生成器是迭代器的一种，yield（）函数,
def frange(start, stop, step):
    x = start
    # while True:
    #    x < stop
    while x < stop:
        # print(x)
        yield x
        x += step


for i in frange(10, 20, 0.5):
    print(i)

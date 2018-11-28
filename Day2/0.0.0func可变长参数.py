#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 10:32
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0func.py
# @Software: PyCharm

# 函数之自定义函数与内置函数
# 函数的参数和关键字参数
# print可以带5个参数，想跳过第二个参数，直接使用第三个参数，必须使用”关键字=“
# print('abc', end='\n\n')
# print('abc')

# def func(a, b, c):
#     print('a= %s' % a)
#     print('b= %s' % b)
#     print('b= %s' % c)
#
#
# # func(1, 2, 3)
#
# # 使用关键字参数可以忽略顺序
# func(1, c=3, b=2)


# 函数的可变长参数，后面的参数是可选的
def howlong(first, *other):
    # return len(first) + len(other)
    # return 1 + len(other)
    print(1 + len(other))

# 至少传递一个参数
# howlong(123, 234, 345)

# TypeError: howlong() missing 1 required positional argument: 'first'
# howlong()


howlong(123)
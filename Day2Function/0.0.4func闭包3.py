#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:59
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.4func闭包3.py
# @Software: PyCharm


# a * x + b = y
def a_line(a, b):
    def arg_y(x):
        return a*x+b
    return arg_y

# a=3, b=5,
# x=10, y=?
# x=20, y=?


line1 = a_line(3, 5)
line2 = a_line(5, 10)
print(line1(10))
print(line1(20))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 14:29
# @Author  : Jianfeng Ding
# @Site    :
# @File    : 0.0.5装饰器4带函数.py
# @Software: PyCharm


def new_tips(x_func, y_func):
    def tips(func):
        def nei(a, b):
            x_func()
            func(a, b)
            y_func()
        return nei

    return tips


def x_func():
    print("start")


def y_func():
    print("stop")


@new_tips(x_func, y_func)
def add(a, b):
    print(a + b)


print(add(8, 5))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 14:06
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.10test.py
# @Software: PyCharm


def func1():
    a = 1
    b = 2
    return a + b
    # 返回值是变量


def sum1(a):
    # 外部函数的变量a被内部函数引用的话，这种方式称为闭包。
    def add(b):
        return a + b

    return add
# 返回值是内部函数的名称（引用）
# add 函数名称的引用
# add() 函数的调用


# 调用的区别
# 使用闭包函数的
func2 = func1()
sum2 = sum1(1)

print(type(func2))
print(type(sum2))
print(sum2(1))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 9:37
# @Author  : Jianfeng Ding
# @Site    :
# @File    : 0.0.5装饰器2.py
# @Software: PyCharm

# #######格式：
# def wai(func):
#     def nei():
#         start
#         func()
#         stop
#
#     return nei


# 装饰器作用打tag

def tips(func):
    def nei(a, b):
        print('start')
        func(a, b)
        print('stop')
        return "I am here!"
        # print(add())一般会输出add函数的返回内容，
        # 因为我们的add函数是被tips函数装饰的，
        # 所以函数nei()返回值为空时，print函数会打印None
    return nei


@tips
def add(a, b):
    print(a + b)


@tips
def multiply(a, b):
    print(a * b)


print(add(4, 5))
print(multiply(4, 5))

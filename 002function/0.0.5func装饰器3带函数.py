#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 10:15
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.5装饰器3带函数.py
# @Software: PyCharm


# 装饰器函数
def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print('start %s %s' % (argv, func.__name__))  # 参数和函数名
            func(a, b)
            print('stop %s' % argv)  # 参数
            return 'I am here!!!!'
        return nei

    return tips


# 取得参数和函数名
@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('mul_module')
def multiply(a, b):
    print(a * b)


print(add(4, 5))
print(multiply(4, 5))

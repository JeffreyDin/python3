#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 9:17
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0sanguoV2.py
# @Software: PyCharm

# 函数调用
def func():
    # 函数体
    print(open('name.txt', encoding="utf8").read())
    print('test func')


func()

# 函数调用之自定义函数
def func2(filename):
    print(open(filename, encoding='utf8').read())
    print('test func')


func2('name.txt')

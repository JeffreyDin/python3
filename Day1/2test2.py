#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 17:43
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test2.py
# @Software: PyCharm

name = ''
while not name:
    name = input('Please enter your name: ')
    print('Hello, {}!'.format(name))
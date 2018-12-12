#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 14:56
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.6func上下文管理器.py
# @Software: PyCharm


# fd = open('neme.txt')
# try:
#     for line in fd:
#         print(line)
# finally:
#     fd.close()

# 上下文管理器
with open(r'E:\Python\Python-primary\Day2\name.txt') as gxs:
    for line in gxs:
        print(line)


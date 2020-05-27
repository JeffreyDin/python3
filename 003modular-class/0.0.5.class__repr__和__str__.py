#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:41
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.2.1.py
# @Software: PyCharm


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


p = Pair('a', 'b')
print(p)
print(str(p))
print(repr(p))
print(type(p))
# print(dir(p))


# <__main__.Pair object at 0x00000214A817C358>
# <class '__main__.Pair'>

# Pair('a', 'b')
# <class '__main__.Pair'>

# (a, b)
# <class '__main__.Pair'>


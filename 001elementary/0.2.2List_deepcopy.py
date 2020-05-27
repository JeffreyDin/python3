#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/27

import copy
person = ['name', ['saving', 1000]]

p1 = person.copy()    # 浅copy，只复制上一层的子列表，子列表是一个独立的内存指针，是一个内存地址，复制的是内存地址
p2 = person[:]
p3 = list(person)

p1[0] = 'alex'
p2[0] = 'A_Wife'
p1[1][1] = 500

print(p1)
print(p2)
print(p3)
# 浅copy ，联合账户，浅copy的三种方式，实际生活中，使用数据库
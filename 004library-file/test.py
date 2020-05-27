#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 14:23
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : test.py
# @Software: PyCharm


import re

p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.match('Name'))
print(p.match('2018-05-10').group(2))
print(p.match('2018-05-10').groups())
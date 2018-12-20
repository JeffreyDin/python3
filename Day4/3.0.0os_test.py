#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 17:29
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3.0.0os_test.py
# @Software: PyCharm

import os

print(os.path.abspath('..'))
print(os.path.exists('F:\System_ISO'))
print(os.path.isfile('users'))
print(os.path.isfile('2.0.0math.py'))
print(os.path.isdir('F:\System_ISO'))
print(os.path.join('E:/Blog', '/c/d'))

from pathlib import Path

p = Path('.')
print(p.resolve())
print(p.is_dir())
# 创建目录
# q = Path('E:/a/b/c')
# Path.mkdir(q, parents=True)

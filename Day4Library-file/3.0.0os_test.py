#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 17:29
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 3.0.0os_test.py
# @Software: PyCharm


# os.path — Common pathname manipulations
import os

print(os.path.abspath('.'))
# 当前的绝对路径
print(os.path.abspath('..'))
# 当前的上级目录
print(os.path.exists('F:\System_ISO'))
# 判断文件(文件夹和文件)是否存在
print(os.path.isfile('users'))
print(os.path.isfile('2.0.0math.py'))
print(os.path.isdir('F:\System_ISO'))
print(os.path.join('E:/Blog' '/moban'))
# 文件拼接
print("--------------")

# pathlib — Object-oriented filesystem paths
from pathlib import Path

p = Path('.')
print(p.resolve())
# 当前的绝对路径
print("--------------")
print(p.is_dir())
# q = Path('E:/a/b/c')
# Path.mkdir(q, parents=True)
# 创建目录
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 8:39
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : sanguo.py
# @Software: PyCharm

# 读取人物名称
f = open('name.txt', encoding="utf8")
data = f.read()
print(data.split("|"))

# 读取兵器的名称
f2 = open('weapon.txt', encoding="utf8")
# data2 = f2.read()
# print(data2)
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        # print(line)
        print(line.strip('\n'))  # strip()函数删除换行符
    i += 1

# 读取三国
f3 = open('sanguo.txt', encoding="GB18030")
print(f3.read().replace('\n', ''))  # replace()函数 替换

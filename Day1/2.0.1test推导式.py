#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 17:10
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test.py
# @Software: PyCharm

# 列表推导式和字典推导式

# 计算1 到 10 偶数的平方
alist = []
for i in range(1, 11):
    if (i % 2) == 0:
        alist.append(i*i)
print(alist)

# 上述不够简洁,列表推导式
blist = [i*i for i in range(1, 11) if(i % 2) == 0]
print(blist)


# cz_num = {}
# for i in chinese_zodiac:
#     cz_num[i] = 0
#
# z_num = {}
# for i in zodiac_name:
#     z_num[i] = 0

# 字典推导式
cz_num = {i: 0 for i in chinese_zodiac}
z_num = {i: 0 for i in zodiac_name}
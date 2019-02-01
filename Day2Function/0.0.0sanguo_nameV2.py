#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 9:36
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0sanguoV2.py
# @Software: PyCharm

import re


def find_item(hero):
    with open('sanguo.txt', encoding="GB18030") as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print("主角%s出现%s次 " % (hero, len(name_num)))

    # return name_num
    return len(name_num)

# 读取人物信息


name_dict = {}
with open('name.txt', encoding='utf8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            # print(n)
            name_num = find_item(n)
            name_dict[n] = name_num
# 字典排序
name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:20])

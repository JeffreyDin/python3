#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/26


names = ["DJ", "ZhangYang", "YanYun", ['alex', 'Jack'], "WangYa", "LiLei"]
# 列表循环
for i in names:
    print(i)


# range(1, 10, 2)


# 浅copy，只复制上一层的子列表，子列表是一个独立的内存指针
# 是一个内存地址，复制的是内存地址
# names2 = names.copy()

# 深copy，占两份独立的地址空间
'''names2 = copy.deepcopy(names)
print(names)
print(names2)
names[0] = "帝姬"
names[3][0] = "ALEX"     # 由于指向同一块地址空间，names[3][0] = names2[3][0]
print(names)
print(names2)'''
# print(names[0:-1:2])  # 跳着切
# print(names[::2])     # 0,-1可省略
# print(names[:])


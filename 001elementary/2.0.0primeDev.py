#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 9:24
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : flag.py
# @Software: PyCharm

# 输出2-100之间的所有素数
# from math import sqrt
# for i in range(2, 101):
#     k = int(sqrt(i))
#     if k+1 < 3:
#         print(i)
#     else:
#         for j in range(2,k+1):
#             if i % j == 0:
#                 break
#             if j == k:
#                 print(i)

# 使用flag变量输出2-100的素数
from math import sqrt
for i in range(2, 101):
    flag = 1
    k = int(sqrt(i))
    for j in range(2, k+1):
        if i % j == 0:
            flag = 0
            break
    if flag == 1:  # 使用flag变量保存当前数是否为素数
        print(i)


for n in range(2, 101):
    for x in range(2, n):
        if n % x == 0:
            # print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, '是质数')

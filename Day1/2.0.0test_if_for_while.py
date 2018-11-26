#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/11/13


# 最简单的条件判断，针对关键字或关键代码块进行判断
# x = 'abc'
# if x == 'abc':
#     print('x的值和abc相等')

# 1.使用for语句输出1-100之间的所有偶数
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

# 2. 使用while语句输出1-100之间能够被3整除的数字
j = 1
while j <= 100:
    if j % 3 == 0:
        print(j)
    j += 1





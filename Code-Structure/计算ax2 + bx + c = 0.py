#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 15:47
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 计算ax2 + bx + c = 0.py
# @Software: PyCharm

# 定义函数
import math


def quadratic(a, b, c):
    q = b * b - 4 * a * c
    if q > 0:
        x1 = (-b + math.sqrt(q)) / a / 2
        x2 = (-b - math.sqrt(q)) / a / 2
        return x1, x2
    elif q == 0:
        x1 = -b / a / 2
        x2 = x1
        return x1, x2
    else:
        pass
        return ()


print('input a,b,c')
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
q = quadratic(a, b, c)
# q = set(list(q))
print('q =',q)
if len(q) == 2:
    for x in q:
        print(x)
elif len(q) == 1:
    for x in q:
        print(x)
else:
    print('None')

# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

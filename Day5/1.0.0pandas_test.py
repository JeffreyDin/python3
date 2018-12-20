#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 13:06
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.0pandas_test.py
# @Software: PyCharm

from pandas import Series, DataFrame

# import pandas as pd

obj = Series([4, 5, 6, -7])
# print(obj)
#
# print(obj.index)
# print(obj.values)
#
# # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'd': 4}
# # int float string tuple

# # 索引,不会像字典一样覆盖重复的键值
# obj2 = Series([3, 4, 5, 6, 6], index=['a', 'c', 'e', 'g', 'g'])
# print(obj2)
# # 修改
# obj2['c'] = 100
# print(obj2)
# # 判断是否存在
# print('a' in obj2)

# 将字典转化成Series
sdata = {'beijing': 3500, 'shanghai': 5400, 'guangzhou': 6500, 'shenzhen': 3000}
obj3 = Series(sdata)
print(obj3)
# 缩写索引
obj3.index = ['bj', 'sh', 'gz', 'sz']
print(obj3)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 15:22
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.2pandas_层次化索引.py
# @Software: PyCharm

from pandas import Series
# from pandas import DataFrame, Series
import numpy as np

data3 = Series(np.random.random(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data3)
# print(data3['b':'c'])
print(data3.unstack())
print(data3.unstack().stack())

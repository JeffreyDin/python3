#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 20:49
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0NumPy_test.py
# @Software: PyCharm

import numpy as np

# arr1 = np.array([2, 3, 4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2, 2.3, 3.4])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1 + arr2)
# print(arr1 * 2)
#
# data = [[1, 2, 3], [4, 5, 6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

# NumPy数组
# print(np.zeros((3, 4)))
# print(np.ones((3, 4)))

# print(np.empty((1, 5, 6)))

# copy
arr4 = np.arange(10)
print(arr4[2:8])

arr4[5:8] = 100
print(arr4[2:8:2])

arr4_slice = arr4[5:8].copy()
arr4_slice[:] = 15
print(arr4_slice)
print(arr4)
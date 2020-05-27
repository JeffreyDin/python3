#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: gxs
@license: (C) Copyright 2016-2019, Light2Cloud (Beijing) Web Service Co., LTD
@contact: dingjianfeng@light2cloud.com
@software: AWS-DJF
@file: 1234.py
@ide: PyCharm
@time: 2019/8/12 22:58
@desc：
"""

# # number = "00100"
# number = "54321"
#
# numlist = [0] * 10  # 0-9
# length = 0
# flag = False
#
# # 计算数字重复次数和长度
# for i in number:
#     if i != '0' or flag :
#         flag = True
#         numlist[int(i)] += 1
#         length += 1
# print('the length of number is {}'.format(length))

nums = []
while len(nums) < 5:
    num = input(">>>").strip().lstrip('0')
    if not num.isdigit():
        continue
    print('The length of {} is {}'.format(num, len(num)))
    nums.append(int(num))
print(nums)

# # sort 方法排序
lst = nums.copy()
lst.sort()  # 就地修改
print(lst, '---------')


# 冒泡法
for i in range(len(nums)):
    flag = False
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            tmp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = tmp
            flag = True
    if not flag:
        break
print(nums, '+++++++++')

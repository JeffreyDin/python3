#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 23:06
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 00Aggregate.py
# @Software: PyCharm

# 将字符串hello中每个字符赋值给一个集合，将这个集合输出到屏幕
# str1 = 'hello'
# # 集合里的元素不能重复
# print(set(str1))

# 交叉测试
list1 = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8]
list1 = set(list1)
print(list1, type(list1))
list2 = set([1, 3, 111, 9])
print(list1, list2)
# 取交集
lss =  list1.intersection(list2)
print(lss)
# 取并集
bingji = list1.union(list2)
print(bingji)
# 取差集
chaji = list1.difference(list2)
print(chaji)
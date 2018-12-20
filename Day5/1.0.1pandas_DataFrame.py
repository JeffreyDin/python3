#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 14:21
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 1.0.1pandas_.py
# @Software: PyCharm


# DataFrame二维数据
# Series 一维数据
from pandas import DataFrame, Series

data = {'city': ['shanghai', 'shanghai', 'shanghai', 'Beijing', 'Beijing'],
        'year': [2016, 2017, 2018, 2019, 2020],
        'pop': [1.5, 1.6, 1.7, 1.8, 1.9]}

frame = DataFrame(data)
# 排序
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame)
# print(frame2)

# # 提取,将二维表格转化成一维数据
# # print(frame2['city'])
# # print(frame2.year)
#
# # 附加新的列
# frame2['new'] = 100
# print(frame2)
# # 附加新的列2
# frame2['cap'] = frame2.city == 'Beijing'
# print(frame2)
#
# # 行列索引的转换
# pop = {'beijing': {2008: 1.5, 2009: 2.0},
#        'shanghai': {2009: 1, 2010: 2.5}}
# frame3 = DataFrame(pop)
# print(frame3)
#
# print(frame3.T)

# # 重新索引,填充不存在值fill_value
# obj4 = Series([4.5, 7.2, -5.2, 3.6], index=['b', 'd', 'c', 'a'])
# obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# print(obj5)
#
# # 填充相邻元素的值
# obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# # print(obj6.reindex(range(6), method='ffill'))
# print(obj6.reindex(range(6), method='bfill'))

# 对无法补全的缺失值，进行删除
from numpy import nan as NA

data = Series([1, NA, 2])
# print(data.dropna())

# # 删除全是缺失值的一行
data2 = DataFrame([[1.0, 6.5, 3.0], [1.0, NA, NA], [NA, NA, NA]])
# print(data2.dropna(how='all'))
# # 删除全是缺失值的一列
# data2[4] = NA
# print(data2)
# print(data2.dropna(axis=1, how='all'))
# 填充缺失值为0,修改的是data2的副本
# data2.fillna(0)
# print(data2.fillna(0))
# 填充缺失值为0,修改的是data2
data2.fillna(0)
print(data2.fillna(0, inplace=True))
print(data2)

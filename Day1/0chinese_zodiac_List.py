#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/11/13

# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# 切片
# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])


year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
# 将列表作为下标
print("狗" in chinese_zodiac)
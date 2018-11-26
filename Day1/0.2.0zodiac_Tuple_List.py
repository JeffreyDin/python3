#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: Jianfeng Ding  Time: 2018/11/13


# 元组,字符串数据不可变更， 列表数据可变更的，可增加删除等
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (2, 15)


# filter() 函数用于过滤序列(列表，元组，字符串),使用 list()来转换成列表
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
print(zodiac_day)
print(list(zodiac_day))
zodiac_len = len(list(zodiac_day)) % 12
print(zodiac_len)
print(zodiac_name[zodiac_len])  # 将列表作为下标




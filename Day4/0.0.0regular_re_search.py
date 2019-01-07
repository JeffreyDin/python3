#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:11
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0regular不完全匹配.py
# @Software: PyCharm

import re

# # 完全匹配后,进行分组
# p = re.compile('....-..-..')
# p = re.compile('(\d+)-(\d+)-(\d+)')
# print(p.match('sss2018-05-10'))

# 不完全匹配,搜索指定的字符串
# match与search
p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.search('sss2018-05-10'))
# print(p.search('aa2018-09-21bb'))

# match与search
# search()的工作方式与 match()完全一致，不同之处在于
# search()会用它的字符串参数，在“任意位置”对给定正则表达式模式搜索第一次出现
# 的匹配情况。如果搜索到成功的匹配，就会返回一个匹配对象； 否则， 返回 None。
print("----------")
# m = re.match('foot', 'bartfoot')  # 匹配失败
m = re.match('foot', 'footbart')   # 匹配成功
if m is not None:
    print(m.group())
print("----------")

m = re.search('foot', 'bartfoot')
if m is not None:
    print(m.group())

# re.findall()完全匹配

# # 替换函数sub()
# phone = '123-456-789  # 这是电话号码'
# p2 = re.sub(r'#.*$', '', phone)
# print(p2)
# p3 = re.sub(r'\D', '', p2)
# print(p3)


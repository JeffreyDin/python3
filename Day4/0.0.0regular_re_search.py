#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 17:11
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0regular不完全匹配.py
# @Software: PyCharm

import re

# 完全匹配后,进行分组
p = re.compile('....-..-..')
p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.match('sss2018-05-10'))

# 不完全匹配,搜索指定的字符串
# match与search
p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.search('sss2018-05-10'))
# print(p.search('aa2018-09-21bb'))

# re.findall()完全匹配

# 替换函数sub()
phone = '123-456-789  # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)
print(p2)
p3 = re.sub(r'\D', '', p2)
print(p3)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 16:28
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.0regular.py
# @Software: PyCharm


# . ^ $ * + ? {m} {m, n} [] | \d \D \s ()
# ^$   空行
# .*?  非贪婪模式

# import re
#
# p = re.compile('ca*t')
# print(p.match('caaaaaaaaaaaat'))

# c[abcd]t
# cat
# cbt
# cct
# cdt

# [0-9]+        \d  表示数字
# 123-456-789   \D  表示不包括数字
# ()   表示分组

import re

p = re.compile('.{3}')
print(p.match('lennnnn'))

# p = re.compile('....-..-..')
p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.match('2018-05-10'))
print(p.match('2018-05-10').group(2))
print(p.match('2018-05-10').groups())
# 取出,并赋值
year, month, day = p.match('2018-05-10').groups()
print(year)
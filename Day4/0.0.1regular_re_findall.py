#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 10:52
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.1regular_re_findall.py
# @Software: PyCharm


# findall
# import re
#
# s = "456123sad 789re3dfheasdf a123fas 123awef q3segd a123dsas"
# re0subject1 = re.compile('\w+\s+')
# print(re0subject1.findall(s))

# import re
#
# s = "456123sad  789re3dfheasdf  a123fas  123awef  q3segd  a123dsas "
# re0subject2 = re.compile('\w+\s+')
# print(re0subject2.findall(s))

# import re
#
# s = "456123sad  789111re3dfheasdf  a123fas  123awef  q3segd  a123dsas "
# # s = "adfad asdfasdf asdfas asdfawef asd adsfas "
# re0subject3 = re.compile('(\w+)\s+\w+')
# print(re0subject3.findall(s))


import re

s = "456123sad  789111re3dfheasdf  a123fas  123awef  q3segd  a123dsas "
# s = "adfad asdfasdf asdfas asdfawef asd adsfas "
re0subject3 = re.compile('((\w+)\s+\w+)')
print(re0subject3.findall(s))
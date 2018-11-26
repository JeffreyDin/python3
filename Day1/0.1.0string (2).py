#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/6/27

name = "my name is {name} and i am {years} old."
print(name.format(name='alex', years=23))   # 格式化
print(name.format_map({'name': 'alex', 'years': 12}))   # 字典，格式化
# print(name.isalnum())
print('123Abc123'.isalnum())      # 判断是否为数字和字母
print('ABCas'.isalpha())          # 判断是否为字母
print('1237'.isdecimal())         # 判断是否为十进制
print('123'.isdigit())            # 判断是否为整数
print('As3adf'.isidentifier())    # 判断是否为一个合法的标识符（变量名）
print('13414'.isnumeric())        # 判断是否为一个数字
print('My Name is'.istitle())     # 判断是每个字符的首字母是否为大写
print('MY NAME IS'.isupper())     # 判断是每个字符是否为大写
print('+'.join(['1', '2', '3']))  # 将列表转化成字符串

print(name.ljust(50, '*'))  # 满足长50，不够在句尾用*补足
print(name.rjust(50, '*'))  # 满足长50，不够在句首用*补足







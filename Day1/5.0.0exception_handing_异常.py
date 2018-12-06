#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 22:03
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 5.0.0exception_handing.py
# @Software: PyCharm

# NameError：变量未定义
# i = j

# SyntaxError：语法错误
# print())

# IndexError: 索引错误之超过索引范围
# a = '123'
# print(a[3])

# KeyError:对应值错误
# d = {'a': 1, 'b': 2}
# print(d['c'])

# ValueError: invalid literal for int() with base 10: 'abc'
# 值误差
# year = int(input('input year: '))

# 捕获异常之ValueError
# try:
#     year = int(input('input year: '))
# except ValueError:
#     print("年份要输入数字！")

# AttributeError: 'int' object has no attribute 'append'
# a = 123
# a.append()
# print(a)

# 同时捕获多个异常, 组合成元组
# except (ValueError, AttributeError, KeyError)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print('0不能作除数 %s' % e)

# 捕获所有的错误
# try:
#     print(1/'a')
# except Exception as e:
#     print('字母不能作除数 %s' % e)

# 自定义异常,通常对文件进行操作
# try:
#     raise NameError('helloError')
# except NameError:
#     print('my custom error!')

try:
    f = open(r'E:\Python\Python-primary\Day1\name.txt')
except Exception as e:
    print(e)
finally:
    f.close()
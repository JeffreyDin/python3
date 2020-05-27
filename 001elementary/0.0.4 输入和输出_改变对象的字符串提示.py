#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 11:13
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.4 输入和输出_改变对象的字符串提示.py
# @Software: PyCharm

# 输出格式美化
# 表达式语句 和 print() 函数.
# (第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用.
# 控制其输出格式 标准模块 string 包含了一些有用的操作, 用以填充字符串至某一给定的宽度;
# 第二种方式是使用 str.format() 方法

# str() 函数意味着返回一个用户易读的表达形式, 而 repr() 则意味着产生一个解释器易读的表达形式 (或者如果没有这样的语法会给出 SyntaxError).
# 对于那些没有特殊表达的对象, str() 将会与 repr() 返回相同的值. 很多的值, 如数字或一些如列表和字典那样的结构,
# 使用这两个函数的结果完全一致. 字符串与浮点型则有两种不同的表达.
# https://docspy3zh.readthedocs.io/en/latest/tutorial/inputoutput.html

# str.format() 的基本使用如下:
#
# >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"
# 括号及其里面的字符 (称作 format field) 将会被 format() 中的参数替换. 在括号中的数字用于指向传入对象在 format() 中的位置.
#
# >>> print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
# >>> print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数.
#
# >>> print('This {food} is {adjective}.'.format(
# ...       food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.
# 位置及关键字参数可以任意的结合:
#
# >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
#                                                        other='Georg'))
# The story of Bill, Manfred, and Georg.
# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
#
# >>> import math
# >>> print('The value of PI is approximately {}.'.format(math.pi))
# The value of PI is approximately 3.14159265359.
# >>> print('The value of PI is approximately {!r}.'.format(math.pi))
# The value of PI is approximately 3.141592653589793.
# 可选项 ':' 和格式标识符可以跟着 field name. 这就允许对值进行更好的格式化. 下面的例子将 Pi 保留到小数点后三位.
#
# >>> import math
# >>> print('The value of PI is approximately {0:.3f}.'.format(math.pi))
# The value of PI is approximately 3.142.
# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度. 用于美化表格时很有用.
#
# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# >>> for name, phone in table.items():
# ...     print('{0:10} ==> {1:10d}'.format(name, phone))
# ...
# Jack       ==>       4098
# Dcab       ==>       7678
# Sjoerd     ==>       4127
# 如果你有一个的确很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情. 最简单的就是传入一个字典, 然后使用方括号 '[]' 来访问键值 :
#
# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
#           'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
# 这也可以通过在 table 变量前使用 ‘**’ 来实现相同的功能.
#
# >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678
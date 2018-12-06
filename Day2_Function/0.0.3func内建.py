#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 20:04
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0.0.3func内建.py
# @Software: PyCharm

# 内建函数
# filter() map()   reduce()  zip()

# filter()内建函数
# filter(function or None, iterable) --> filter object
a = [1, 2, 3, 4, 5, 6]
list(filter(lambda x: x > 2, a))
# >>> a = [1, 2, 3, 4, 5, 6]
# # >>> list(filter(lambda x: x > 2, a))
# # [3, 4, 5, 6]

# map()内建函数
# map(func, *iterables) --> map object
# >>> a = [1, 2, 3, 4, 5, 6]
# >>> map(lambda x:x, a)
# <map object at 0x000002A183CD3F60>
# >>> list(map(lambda x:x+1, a))
# [2, 3, 4, 5, 6, 7]
# >>> b = [4, 5, 6]
# >>> list(map(lambda x,y:x+y, a,b))
# [5, 7, 9]

# reduce内建函数
# >>> from functools import reduce
# >>> help(reduce)
#
# >>> from functools import reduce
# >>> reduce(lambda x,y: x+y, [2, 3, 4], 1)
# 10
# >>> ((1+2)+3)+4

# zip内建函数，对字典的键值对对调
# >> > for i in zip((1, 2, 3), (4, 5, 6)):
#     print(i)
#
# (1, 4)
# (2, 5)
# (3, 6)
# >> >

# >>> dicta = {'a':'aa', 'b':'bb'}
# >> > print(dicta.keys())
# dict_keys(['a', 'b'])
# >> > print(dicta.values())
# dict_values(['aa', 'bb'])
#
# >> > dictb = zip(dicta.values(), dicta.keys())
# >> > print(dict(dictb))
# {'aa': 'a', 'bb': 'b'}



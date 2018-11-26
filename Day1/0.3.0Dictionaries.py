#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 15:58
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 00Dictionaries.py
# @Software: PyCharm

# 映射-字典{"哈希"："对象"}
# dict1 = {}
# print(type(dict1))

dict2 = {'x': 1, 'y': 2}
pass
dict2['z'] = 3
print(dict2)

# 1.定义一个字典，分别使用a，b，c，d作为字典的关键字，值为任意内容
dict1 = { ' a ': ' aa ', ' b ': ' xyz ', ' c ': ' Helo ', ' d ': 123 }
pass
# 2为该字典增加一个元素'C'： '蛋糕'后，将字典输出到屏幕
# 字典的键不能重复，否则会覆盖掉相同键的值
dict1[' ç '] ='蛋糕'
# 打印（ dict1）
print(dict1)
# 3取出字典中关键字为d的值
print(dict1[' d '])

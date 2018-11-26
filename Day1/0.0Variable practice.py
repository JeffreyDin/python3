#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 15:06
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 0Variable practice.py
# @Software: PyCharm

# 变量的定义和使用
# 使用Python计算100美元兑换的人民币数量并用print( )进行输出
# 定义美元
dollar = 100
# 定义汇率
exchange = 6.5102
# 输出结果
print('{dol}美元兑换的人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * exchange))


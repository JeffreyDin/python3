#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20

print("Djf".lower())    # 将大写字母变小写
print("djf".upper())    # 将小写字母变大写
print('------')
print("   \ndjf".lstrip())    # 去左边的空格和回车
print("DJF\n     ".rstrip())    # 去右边的空格和回车
print("    DJF\n".strip())    # 去两边的空格和回车
print('------')
p = str.maketrans("abcdef",'123456')
print("alex li".translate(p))        # 对应字母替换,密钥
print('------')
print("alex li".replace('l', 'L'))  # 对应字母替换
print("alex li".replace('l', 'L', 1))  # 对应字母替换
print('------')
print("alex li".rfind('l'))    # 从左向右,最后一个l的下标
print("al exli li".split('l'))    # 按照分隔符，将字符串分成列表
print('1+2+3+4'.split('+'))
print('1+2\n+3+4'.splitlines())   # 换行
print("Alex Li".swapcase())       # 大小写变换
print("alex li".title())          # 首字母变大写

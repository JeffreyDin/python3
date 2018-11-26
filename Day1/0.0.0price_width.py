#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Farr Ding  Time: 2018/7/20

width = int(input('Please enter width: '))
price_width = 7
# 指定price符的字段宽度，默认以空格填充
item_width = width - price_width
header_fmt = '{{:^{}}}{{:>{}}}'.format(item_width, price_width)
# 要指定左对齐、右对齐和居中，可分别使用<  >和^ 。
fmt = '{{:<{}}}{{:$>{}.2f}}'.format(item_width, price_width)
# 可以使用填充字符来扩充对齐说明符，这样将使用指定的字符而不是默认的空格来填充。
# "{:$^15}".format(" WIN BIG ")   ——>$$$ WIN BIG $$$
# .2f  将值(价格)的格式设置为包含2位小数的浮点数。
print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))
print('=' * width)

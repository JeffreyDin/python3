#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 10:47
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 00test.py
# @Software: PyCharm

# rang()函数，指定区间的值，遍历不同的步长；创建列表
# for i in range(5, 10):
# for i in range(0, 10, 3):
#     print(i)
#
# list(range(5))


# len()函数+range函数遍历序列索引
# a = ['Google', 'Baidu', 'Gunxiaoshi', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])

# filter()函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象。
# 如果要转换为列表，可以使用 list() 来转换。
# 接收两个参数，第一个为函数，第二个为序列，
# 序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
# filter(function, iterable)  （判断函数，可迭代对象）

# >> > a = (1, 2, 3, 4, 5, 6, 7, 8)
# >> > b = 4
# >> > filter(lambda x: x < b, a)
# < filter object at 0x0000029C77278B38 >
# >> > list(filter(lambda x: x < b, a))  # 取出a中小于4的元素
# [1, 2, 3]
# >> > b = 6
# >> > list(filter(lambda x: x < b, a))  # 取出a中小于6的元素
# [1, 2, 3, 4, 5]
# >> > len(list(filter(lambda x: x < b, a)))  # 取出a中小于6的元素的个数
# 5
# >> >

# 过滤出列表中的所有奇数：
# 声明函数的那一行的上方必须有两行的空行！！！！！！！！！！！
# def is_odd(n):
#     return n % 2 == 1
#
#
# tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# newlist = list(tmplist)
# print(tmplist)
# print(newlist)

# 过滤出1~100中平方根是整数的数
import math


def is_sqr(x):
    return math.sqrt(x) % 1 == 0


tmplist = filter(is_sqr, range(1, 101))
newlist = list(tmplist)
print(newlist)

# format()函数
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

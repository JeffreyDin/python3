#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/11/20 15:29
# @Author  : Jianfeng Ding
# @Site    : 
# @File    : 2test-while.py
# @Software: PyCharm


# 斐波纳契数列,编程第一步。
# b=1,a:1 b:1.  b=1,a:1 b:2.   b=2,a:2 b:3.   b=3,a:3 b:5.   b=5,a:5 b:8.  b=8,a:8 b:13.  b=13
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a+b


# while循环之计算1到100的总和
n = 100
summer = 0
counter = 1
while counter <= n:
    summer = summer + counter
    counter += 1
print("1到%d之和为：%d" % (n, summer))

# while无限循环
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
# print("Good bye!")

# while 循环使用 else 语句
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count = count + 1
# else:
#     print(count, "大于或等于5 ")


# while循环
# import time
# num = 5
# while True:
#     num = num + 1
#     if num == 10:
#         # continue
#         break
#     print(num)
#     time.sleep(1)

